import typing
import pandas as pd
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.dependencies import get_db

router = APIRouter(
    prefix="/likes",
    tags=["Likes"]
)


@router.get("/under-30K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['likes'] < 3e4]['likes'].count()
    percentage = round(count / df['likes'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }

@router.get("/under-50K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['likes'] < 5e4]['likes'].count()
    percentage = round(count / df['likes'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }

@router.get("/under-100K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['likes'] < 10e4]['likes'].count()
    percentage = round(count / df['likes'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }


@router.get("/under-150K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['likes'] < 15e4]['likes'].count()
    percentage = round(count / df['likes'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }
