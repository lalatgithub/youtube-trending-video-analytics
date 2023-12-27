### YouTube Trending Video Analytics

This repository shows some interesting video analytics from YouTube based in United States for the year 2017 and 2018.
These analytics are based on the stats file from Kaggle [here](https://www.kaggle.com/datasets/datasnaek/youtube-new)

The repository has Jupyter Notebook to visualize the stats in browser and also has a FastAPI app to serve some interesting stats using REST endpoints.
Both the Jupyter and FastAPI source code is dockerized and could be run through docker compose to avoid running manual steps for installing dependencies, CLIs and servers.

#### Tech Stack
* Python 3.11
* Pandas
* Matplotlib
* Numpy
* FastAPI
* SQLAlchemy
* SQLite
* Jupyter
* Uvicorn
* Docker

#### Setup and Run project
Follow these steps to setup and run both FastAPI app and Jupyter notebook

Clone this repo
```
git clone https://github.com/lalatgithub/youtube-trending-video-analytics.git
```

Switch to cloned dir and run.

```
cd youtube-trending-video-analytics
```

*NOTE: If you want to run FastAPI app and Jupyter on a different port, Please update `.env` accordingly in root dir.*
```
docker compose up
```

<img src="https://media.giphy.com/media/lGZCPXd5quy0xu9p3r/giphy.gif" width="400" height="400" />


once docker compose runs successfully, you should be able to fetch data from REST endpoints here [http://localhost:8000/](http://localhost:8000/). You can see that you have a `./analytics.db` file in the project root dir.
The analytics are loaded from `./datasets/USVideos.csv` during the app startup.

The Jupyter notebook can be access here
[http://localhost:8888/notebooks/YouTube%20Trending%20Videos.ipynb](http://localhost:8888/notebooks/YouTube%20Trending%20Videos.ipynb)
