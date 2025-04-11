from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Optional


class Base(DeclarativeBase):
    pass

class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(nullable=True)
    user1: Mapped[Optional[str]] = mapped_column(nullable=True)
    user2: Mapped[Optional[str]] = mapped_column(nullable=True)
    user3: Mapped[Optional[str]] = mapped_column(nullable=True)