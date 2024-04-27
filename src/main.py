from fastapi import FastAPI
from .api import country


app = FastAPI()
# Include the routers
app.include_router(country.router)
