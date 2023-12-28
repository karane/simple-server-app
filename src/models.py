from pydantic import BaseModel

# Pydantic model to define the schema of the data
class Item(BaseModel):
    id: int = None
    name: str
    description: str = None