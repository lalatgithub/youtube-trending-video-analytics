import typing
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.orm import schemas, crud
from app.dependencies import get_db

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@router.get("/", response_model=typing.List[schemas.Video])
def get_videos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    videos = crud.get_videos(db, skip=skip, limit=limit)
    return videos


@router.get("/video/{video_id}", response_model=schemas.Video)
def get_video_by_youtube_video_id(video_id: str, db: Session = Depends(get_db)):
    video = crud.get_video(db, video_id=video_id)

    if video is None:
        raise HTTPException(status_code=404, detail="video not found")

    return video
