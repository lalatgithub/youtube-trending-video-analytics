from pydantic import BaseModel, AnyHttpUrl, PastDate


class Video(BaseModel):
    video_id: str
    trending_date: PastDate
    title: str
    channel_title: str
    category_id: int
    views: int
    likes: int
    dislikes: int
    comment_count: int
    thumbnail_link: AnyHttpUrl
    comments_disabled: bool
    ratings_disabled: bool
    video_error_or_removed: bool
    description: str | None = None
    title_length: int
    category_name: str
    publishing_day: str
    publishing_hour: int

    class Config:
        from_attributes = True
