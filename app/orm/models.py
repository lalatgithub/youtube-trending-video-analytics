from sqlalchemy_utils import URLType
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.types import ARRAY, Date

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
