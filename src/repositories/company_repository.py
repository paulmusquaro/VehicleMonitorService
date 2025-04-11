from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.entity.models import Company


async def create_company(db: AsyncSession, company: Company) -> Company:
    db.add(company)
    await db.commit()
    await db.refresh(company)
    return company

async def get_company(db: AsyncSession, company_id: int) -> Company | None:
    result = await db.execute(select(Company).filter(Company.id == company_id))
    return result.scalars().first()

async def get_all_companies(db: AsyncSession) -> list[Company]:
    result = await db.execute(select(Company))
    return result.scalars().all()

async def update_company(db: AsyncSession, company: Company, update_data: dict) -> Company:
    for key, value in update_data.items():
        setattr(company, key, value)
    await db.commit()
    await db.refresh(company)
    return company

async def delete_company(db: AsyncSession, company: Company) -> None:
    await db.delete(company)
    await db.commit()
