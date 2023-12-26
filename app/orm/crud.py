from sqlalchemy.orm import Session

from . import models


def get_video(db: Session, video_id: str):
    return db.query(models.Video).filter(models.Video.video_id == video_id).first()


def get_video_by_pk(db: Session, pk: int):
    return db.query(models.Video).filter(models.Video.id == pk).first()


def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Video).offset(skip).limit(limit).all()
