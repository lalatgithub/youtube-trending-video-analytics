from sqlalchemy.types import Date
from sqlalchemy.orm import Session
from sqlalchemy_utils import URLType
from sqlalchemy import Boolean, Column, Integer, String, func, extract

from .database import Base


class Video(Base):
    __tablename__ = "videos"

    video_id = Column(String, primary_key=True, index=True)
    trending_date = Column(Date)
    title = Column(String)
    channel_title = Column(String)
    category_id = Column(Integer)
    views = Column(Integer)
    likes = Column(Integer)
    dislikes = Column(Integer)
    comment_count = Column(Integer)
    thumbnail_link = Column(URLType)
    comments_disabled = Column(Boolean)
    ratings_disabled = Column(Boolean)
    video_error_or_removed = Column(Boolean)
    description = Column(String, nullable=True)
    title_length = Column(Integer)
    category_name = Column(String)
    publishing_day = Column(String)
    publishing_hour = Column(Integer)


    @classmethod
    def get_by_youtube_video_id(cls, db: Session, video_id: str):
        return db.query(cls).filter(cls.video_id == video_id).first()

    @classmethod
    def get_list(cls, db: Session, year: int = None, skip: int = 0, limit: int = 100):
        if year:
            by_year_filter = extract('year', cls.trending_date) == year
            return db.query(cls).filter(by_year_filter).offset(skip).limit(limit)

        return db.query(cls).offset(skip).limit(limit).all()

    @classmethod
    def most_viewed(cls, db: Session, year: int = None):
        most_views_filter = (cls.views == db.query(func.max(cls.views)))
        if year:
            by_year_filter = (extract('year', cls.trending_date) == year)
            return db.query(cls).filter(by_year_filter).order_by(cls.views.desc()).first()

        return db.query(cls).filter(most_views_filter).first()

    @classmethod
    def most_liked(cls, db: Session, year: int = None):
        most_likes_filter = (cls.likes == db.query(func.max(cls.likes)))
        if year:
            by_year_filter = (extract('year', cls.trending_date) == year)
            return db.query(cls).filter(by_year_filter).order_by(cls.likes.desc()).first()

        return db.query(cls).filter(most_likes_filter).first()
    
    @classmethod
    def most_disliked(cls, db: Session, year: int = None):
        most_dislikes_filter = (cls.dislikes == db.query(func.max(cls.dislikes)))
        if year:
            by_year_filter = (extract('year', cls.trending_date) == year)
            return db.query(cls).filter(by_year_filter).order_by(cls.dislikes.desc()).first()

        return db.query(cls).filter(most_dislikes_filter).first()

    @classmethod
    def most_commented(cls, db: Session, year: int = None):
        most_comments_filter = (cls.comment_count == db.query(func.max(cls.comment_count)))
        if year:
            by_year_filter = (extract('year', cls.trending_date) == year)
            return db.query(cls).filter(by_year_filter).order_by(cls.comment_count.desc()).first()

        return db.query(cls).filter(most_comments_filter).first()
