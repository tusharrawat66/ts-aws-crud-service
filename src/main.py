from . import app

# Define your routes and API endpoints here
@app.get("/")
async def get_equipment():
    return {"message": "Hello from Service 1!"}
