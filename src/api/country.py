from fastapi import APIRouter, HTTPException
from ..services.dynamoDb import dynamodb_handler
from ..services.utils import schema_dump
from ..schema.Countryschema import CountryCreate,CountryRead,CountryUpdate
from ..config import config



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
        "country": country.country,
        "capital": country.capital,
        "continent": country.continent,
        "population": country.population,
        "code": country.code
    }
    response = table.put_item(Item=new_item)
    return schema_dump(CountryRead(**new_item))



@router.patch("/update/{id}", response_model=CountryCreate, status_code=201)
def update_countries(id: str, country: CountryUpdate):
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