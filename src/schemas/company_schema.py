from pydantic import BaseModel, EmailStr
from typing import Optional

class CompanyBase(BaseModel):
    name: str
    address: Optional[str] = None
    email: EmailStr
    phone: Optional[str] = None
    user1: Optional[str] = None
    user2: Optional[str] = None
    user3: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    pass

class CompanyDeleteResponse(BaseModel):
    message: str

class CompanyOut(CompanyBase):
    id: int

    class Config:
        from_attributes = True
