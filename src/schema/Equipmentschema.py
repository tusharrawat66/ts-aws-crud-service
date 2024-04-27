from pydantic import BaseModel


class EquipmentPydanticModel(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None