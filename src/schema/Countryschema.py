from pydantic import BaseModel


class CountryCreate(BaseModel):
    id: int
    country: str
    capital: str
    continent: str
    population: int
    code: int

class CountryUpdate(BaseModel):
    capital: str
    population: int

class CountryRead(CountryCreate):
    id: int

 