import logging
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI

from app.orm import models
from app.orm.database import engine
from app.dependencies import get_db
from app.analytics import load_youtube_analytics_into_db
from app.routers import likes, comments, categories, channels, views

models.Base.metadata.create_all(bind=engine)

log = logging.getLogger(__file__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_conn = engine.connect()
    load_youtube_analytics_into_db(db_conn)
    yield


app = FastAPI(
            lifespan=lifespan,
            dependencies=[Depends(get_db)],
            title="YouTube Trending Video Analytics",
            description="This is a demo for YouTube Trending Video Analytics",
            version="0.0.1",
            contact={
                "name": "Lal",
                "url": "https://www.linkedin.com/in/iamlal/",
                "email": "lalzadamohmand@gmail.com",
            },
            docs_url="/"
    )


app.include_router(likes.router)
app.include_router(views.router)
app.include_router(comments.router)
app.include_router(categories.router)
app.include_router(channels.router)
