from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Comic
from app.schemas import ComicOut

router = APIRouter(prefix="/comics", tags=["comics"])


@router.get("", response_model=List[ComicOut])
def get_comics(db: Session = Depends(get_db)):
    return db.query(Comic).all()
