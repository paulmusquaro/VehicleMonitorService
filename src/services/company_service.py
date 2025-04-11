from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.company_schema import CompanyCreate, CompanyUpdate
from src.entity.models import Company
from src.repositories import company_repository


async def create_company(db: AsyncSession, company_data: CompanyCreate) -> Company:
    company = Company(**company_data.dict())
    return await company_repository.create_company(db, company)


async def get_company(db: AsyncSession, company_id: int) -> Company | None:
    return await company_repository.get_company(db, company_id)


async def get_all_companies(db: AsyncSession) -> list[Company]:
    return await company_repository.get_all_companies(db)


async def update_company(db: AsyncSession, company_id: int, company_data: CompanyUpdate) -> Company | None:
    company = await company_repository.get_company(db, company_id)
    if not company:
        return None
    return await company_repository.update_company(db, company, company_data.dict(exclude_unset=True))


async def delete_company(db: AsyncSession, company_id: int) -> Company | None:
    company = await company_repository.get_company(db, company_id)
    if not company:
        return None
    await company_repository.delete_company(db, company)
    return company
