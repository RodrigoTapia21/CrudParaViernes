from pydantic import BaseModel


class Product(BaseModel):
    name: str
    detail: str | None = None
    price: float
    tags: str