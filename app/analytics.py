import json
import logging
import pandas as pd
from datetime import datetime

from app.orm.database import engine

log = logging.getLogger(__file__)


def load_from_dataframe_into_db():

    db_conn = engine.connect()

    log.info('Loading YouTube analytics into database. Hold on...')

    df = pd.read_csv('./dataset/USvideos.csv')
    df["title_length"] = df["title"].apply(lambda x: len(x))

    with open("./dataset/US_category_id.json") as file:
        categories = json.load(file)["items"]

    cat_dict = {}

    for cat in categories:
        cat_dict[int(cat["id"])] = cat["snippet"]["title"]

    df['category_name'] = df['category_id'].map(cat_dict)

    df["trending_date"] = df["trending_date"].apply(
        lambda x: datetime(int('20' + x[:2]), int(x[6:8]), int(x[3:5])).date())

    df["publishing_day"] = df["publish_time"].apply(
        lambda x: datetime.strptime(x[:10], "%Y-%m-%d").date().strftime('%a'))

    df["publishing_hour"] = df["publish_time"].apply(lambda x: x[11:13])
    df.drop(labels='publish_time', axis=1, inplace=True)

    df.to_sql('videos', db_conn, if_exists='replace', index=False)
