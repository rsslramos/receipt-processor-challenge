from pydantic import BaseModel, Field

class ReceiptItem(BaseModel):
    shortDescription: str = Field(pattern=r'^[\w\s\-]+$')
    price: str = Field(pattern=r'^\d+\.\d{2}$')

class ReceiptRequest(BaseModel):
    retailer: str = Field(pattern=r'^[\w\s\-&]+$')
    purchaseDate: str = Field(pattern=r'^\d{4}-\d{2}-\d{2}$')
    purchaseTime: str = Field(pattern=r'^\d{2}:\d{2}$')
    items: list[ReceiptItem] = Field(min_length=1)
    total: str = Field(pattern=r'^\d+\.\d{2}$') 