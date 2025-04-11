from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.schemas.company_schema import CompanyCreate, CompanyUpdate, CompanyOut, CompanyDeleteResponse
from src.services import company_service
from src.database.database import get_db

router = APIRouter(prefix="/companies", tags=["companies"])


@router.post("/", response_model=CompanyOut)
async def create_company(company: CompanyCreate, db: AsyncSession = Depends(get_db)):
    return await company_service.create_company(db, company)


@router.get("/", response_model=List[CompanyOut])
async def read_companies(db: AsyncSession = Depends(get_db)):
    return await company_service.get_all_companies(db)


@router.get("/{company_id}", response_model=CompanyOut)
async def read_company(company_id: int, db: AsyncSession = Depends(get_db)):
    company = await company_service.get_company(db, company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.put("/{company_id}", response_model=CompanyOut)
async def update_company(company_id: int, company: CompanyUpdate, db: AsyncSession = Depends(get_db)):
    updated = await company_service.update_company(db, company_id, company)
    if not updated:
        raise HTTPException(status_code=404, detail="Company not found")
    return updated


@router.delete("/{company_id}", response_model=CompanyDeleteResponse)
async def delete_company(company_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await company_service.delete_company(db, company_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Company not found")
    return CompanyDeleteResponse(message=f"Company with ID {company_id} successfully deleted")
