#!/bin/sh

uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT --reload --log-config=logging.yaml &

python -c "from app import analytics; analytics.load_from_dataframe_into_db()"

jupyter trust "./notebook/YouTube Trending Videos.ipynb"
jupyter notebook --ip 0.0.0.0 --port $JUPYTER_PORT --no-browser --ServerApp.token="" --ServerApp.password="" --notebook-dir ./notebook
