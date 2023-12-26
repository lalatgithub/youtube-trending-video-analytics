import typing
import pandas as pd
from collections import Counter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.dependencies import get_db

router = APIRouter(
    prefix="/common",
    tags=["Common"]
)


@router.get("/most-common-words-in-video-titles", response_model=list[dict])
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    title_words = list(df["title"].apply(lambda x: x.split()))
    title_words = [x for y in title_words for x in y]
    return [{'word': count[0], 'count': count[1]} for count in Counter(title_words).most_common(25)]


@router.get("/channels-with-most-trending-videos", response_model=dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    df = df.groupby("channel_title").size().reset_index(name="video_count").sort_values("video_count", ascending=False).set_index('video_count').head(20)
    return df.to_dict()['channel_title']



@router.get("/categories-with-most-trending-videos", response_model=dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    return df["category_name"].value_counts().to_frame().to_dict()['count']


@router.get("/publish-time-of-most-trending-videos", response_model=dict)
def get_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    df = df["publishing_day"].value_counts().to_frame().rename(columns={"index": "publishing_day", "publishing_day": "No_of_videos"})
    return df.to_dict()['count']