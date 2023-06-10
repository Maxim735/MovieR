import uvicorn
from fastapi import FastAPI, APIRouter, Query
import warnings
import pandas as pd
from pyngrok import ngrok
import nest_asyncio

from views.charts_view import charts_router
from views.data_view import data_router
from views.recommendations_view import recs_router
from views.user_view import user_router

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

app = FastAPI()

app.include_router(charts_router)
app.include_router(data_router)
app.include_router(recs_router)
app.include_router(user_router)

ngrok_tunnel = ngrok.connect(8000)
print(ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
