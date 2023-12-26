import typing
import pandas as pd
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.dependencies import get_db

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@router.get("/under-5K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['comment_count'] < 5e3]['comment_count'].count()
    percentage = round(count / df['comment_count'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }

@router.get("/under-15K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['comment_count'] < 15e3]['comment_count'].count()
    percentage = round(count / df['comment_count'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }

@router.get("/under-25K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['comment_count'] < 25e3]['comment_count'].count()
    percentage = round(count / df['comment_count'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }


@router.get("/under-50K", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['comment_count'] < 50e3]['comment_count'].count()
    percentage = round(count / df['comment_count'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }
