from typing import Any, Dict
from pydantic import BaseModel

def schema_dump(model: BaseModel) -> Dict[str, Any]:
    """
    Dump a Pydantic model to a dictionary representation.

    Args:
        model (BaseModel): The Pydantic model to be dumped.

    Returns:
        Dict[str, Any]: A dictionary representation of the Pydantic model.
    """
    data = model.dict()
    return data