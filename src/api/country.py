from fastapi import APIRouter, HTTPException
from src.services.dynamoDb import dynamodb_handler
from src.services.utils import schema_dump
from src.schema.Countryschema import CountryCreate,CountryRead,CountryUpdate
from src.config import config



router = APIRouter( 
    prefix="/api",
    tags=["country"],
)

TABLE_NAME = config.get("TABLE_NAME")

@router.get("/", response_model=list[CountryRead])
def get_countries():
    table = dynamodb_handler(TABLE_NAME)

    # For example, you can fetch all items from the DynamoDB table
    items = table.scan()["Items"]
    
    # Map the items to CountryRead models
    countries = [CountryRead(**item) for item in items]
    
    return countries


@router.post("/create", response_model=CountryCreate, status_code=201)
def create_countries(country: CountryCreate):
    table = dynamodb_handler(TABLE_NAME)
    new_item = {
        "id": country.id,
        "country": country.country,
        "capital": country.capital,
        "continent": country.continent,
        "population": country.population,
        "code": country.code
    }

    required_keys = ["country", "capital", "continent", "population", "code"]
    missing_keys = [key for key in required_keys if key not in new_item]
    print(f"NEW ITEM: {new_item}")
    if missing_keys:
        error_message = f"Missing required keys: {', '.join(missing_keys)}"
        raise HTTPException(status_code=400, detail=error_message)

    try:
        response = table.put_item(Item=new_item)
        print(f"RESPONSE:  {response}")
        return schema_dump(CountryRead(**new_item))
    except Exception as e:
        print(f"Error putting item into DynamoDB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    



@router.patch("/update/{id}", response_model=CountryRead, status_code=201)
def update_countries(id, country: CountryUpdate):
    table = dynamodb_handler(TABLE_NAME)
    key = {"id": id}
    # Implement your item creation logic here
    try:
        # Fetch the existing item
        response = table.get_item(Key=key)
        if "Item" not in response:
            raise HTTPException(status_code=404, detail="Country not found")
        
        # Update the existing item
        update_expression = "SET capital = :capital, population = :population"
        expression_attributes = {
            ":capital": country.capital,
            ":population": country.population
        }
        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attributes,
            ReturnValues="UPDATED_NEW"
        )
        updated_item = response["Attributes"]
        return CountryRead(**updated_item)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))