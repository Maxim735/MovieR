from engine.recs_engine import RecsEngine
import pandas as pd
import warnings
import sqlite3

warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

app = RecsEngine()
# app.parse_data(films_amount=10000)
# app.convert_data()
# app.process_data()
