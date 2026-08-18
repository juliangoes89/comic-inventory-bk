from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Editorial
from app.schemas import EditorialOut

router = APIRouter(prefix="/editoriales", tags=["editoriales"])


@router.get("", response_model=List[EditorialOut])
def get_editoriales(db: Session = Depends(get_db)):
    return db.query(Editorial).all()
