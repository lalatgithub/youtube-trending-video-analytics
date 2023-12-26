import typing
import pandas as pd
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.dependencies import get_db

router = APIRouter(
    prefix="/views",
    tags=["Views"]
)


@router.get("/under-1M", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['views'] < 1e6]['views'].count()
    percentage = round(count / df['views'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }

@router.get("/under-1.5M", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['views'] < 1.5e6]['views'].count()
    percentage = round(count / df['views'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }

@router.get("/under-2M", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['views'] < 2e6]['views'].count()
    percentage = round(count / df['views'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }


@router.get("/under-5M", response_model=typing.Dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    count =  df[df['views'] < 5e6]['views'].count()
    percentage = round(count / df['views'].count() * 100, 2)
    return {
        'videos_count': int(count),
        'percentage': f'{percentage}%'
    }
