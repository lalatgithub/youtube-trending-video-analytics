import pandas as pd
from collections import Counter
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_db
from app.orm import schemas, models

router = APIRouter(
    prefix="/common",
    tags=["Common"]
)


@router.get("/video/{youtube-id}", response_model=schemas.Video)
def get_video_by_youtube_video_id(youtube_id: str, db: Session = Depends(get_db)):
    video = models.Video.get_by_youtube_video_id(db, youtube_id)

    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video


@router.get("/video/list", response_model=list[schemas.Video])
def get_video_list(year: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return models.Video.get_list(db, year, skip, limit)


@router.get("/most-viewed-video", response_model=schemas.Video)
def get_most_viewed_video(year: int = None, db: Session = Depends(get_db)):
    video = models.Video.most_viewed(db, year)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video


@router.get("/most-liked-video", response_model=schemas.Video)
def get_most_liked_video(year: int = None, db: Session = Depends(get_db)):
    video = models.Video.most_liked(db, year)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video


@router.get("/most-disliked-video", response_model=schemas.Video)
def get_most_disliked_video(year: int = None, db: Session = Depends(get_db)):
    video = models.Video.most_disliked(db, year)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video

@router.get("/most-commented-video", response_model=schemas.Video)
def get_most_commented_video(year: int = None, db: Session = Depends(get_db)):
    video = models.Video.most_commented(db, year)
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    return video


@router.get("/most-common-words-in-video-titles", response_model=list[dict])
def get_common_words_in_titles(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    title_words = list(df["title"].apply(lambda x: x.split()))
    title_words = [x for y in title_words for x in y]
    return [{'word': count[0], 'count': count[1]} for count in Counter(title_words).most_common(25)]


@router.get("/channels-with-most-trending-videos", response_model=dict)
def get_channels_with_most_trending_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    df = df.groupby("channel_title").size().reset_index(name="video_count").sort_values("video_count", ascending=False).set_index('video_count').head(20)
    return df.to_dict()['channel_title']



@router.get("/categories-with-most-trending-videos", response_model=dict)
def get_categories_with_most_trending_videos(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    return df["category_name"].value_counts().to_frame().to_dict()['count']


@router.get("/publish-time-of-most-trending-videos", response_model=dict)
def get_trending_videos_publish_time(db: Session = Depends(get_db)):
    df = pd.read_sql_query("SELECT * FROM videos", db.connection())
    df = df["publishing_day"].value_counts().to_frame().rename(columns={"index": "publishing_day", "publishing_day": "No_of_videos"})
    return df.to_dict()['count']
