from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas
from sqlalchemy.orm import selectinload 

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    db_user = models.User(name=user.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    return result.scalars().first()

async def create_proposal(db: AsyncSession, proposal: schemas.ProposalCreate):
    db_proposal = models.Proposal(**proposal.dict())
    db.add(db_proposal)
    await db.commit()
    await db.refresh(db_proposal)

    # Reload with user relation
    result = await db.execute(
        select(models.Proposal)
        .options(selectinload(models.Proposal.user))
        .where(models.Proposal.id == db_proposal.id)
    )
    return result.scalars().first()

async def get_proposals(db: AsyncSession):
    result = await db.execute(
        select(models.Proposal)
        .options(selectinload(models.Proposal.user))  # <- Eager load the related user
        .order_by(models.Proposal.timestamp.desc())
    )
    return result.scalars().all()

async def get_proposals(db: AsyncSession):
    result = await db.execute(select(models.Proposal).order_by(models.Proposal.timestamp.desc()))
    return result.scalars().all()
