from fastapi import FastAPI
from api import country
from dotenv import dotenv_values


app = FastAPI()
config = dotenv_values(".env")
# Include the routers
app.include_router(country.router)
