import logging
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

from app.orm import models
from app.orm.database import engine
from app.dependencies import get_db
from app.analytics import load_from_dataframe_into_db
from app.routers import likes, comments, views, common

models.Base.metadata.create_all(bind=engine)

log = logging.getLogger(__file__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_conn = engine.connect()
    load_from_dataframe_into_db(db_conn)
    yield


app = FastAPI(
            lifespan=lifespan,
            dependencies=[Depends(get_db)],
            title="YouTube Trending Video Analytics",
            description="This is a demo for YouTube Trending Video Analytics [2017 & 2018], United States",
            version="0.0.1",
            contact={
                "name": "Lal",
                "url": "https://www.linkedin.com/in/iamlal/",
                "email": "lalzadamohmand@gmail.com",
            },
            docs_url="/"
    )


app.include_router(common.router)
app.include_router(likes.router)
app.include_router(views.router)
app.include_router(comments.router)
