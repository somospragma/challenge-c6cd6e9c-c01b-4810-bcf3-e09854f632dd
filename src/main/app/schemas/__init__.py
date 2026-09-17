from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: str = Field(..., min_length=1, max_length=100)

class ProductUpdate(BaseModel):
    name: str = Field(None, min_length=1, max_length=100)
    price: float = Field(None, gt=0)
    stock: int = Field(None, ge=0)
    category: str = Field(None, min_length=1, max_length=100)

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: str