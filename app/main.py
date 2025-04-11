from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app import models, schemas, crud
from app.database import engine, Base, get_db
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from app.models import Proposal


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter dev mode
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/proposals/", response_model=schemas.Proposal)
async def create_proposal(proposal: schemas.ProposalCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_proposal(db, proposal)

@app.get("/proposals/", response_model=list[ProposalOut])
async def get_proposals(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Proposal).options(selectinload(Proposal.user))
    )
    proposals = result.scalars().all()
    return proposals