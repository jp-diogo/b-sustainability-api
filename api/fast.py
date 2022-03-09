from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pandas as pd
from keras.models import load_model
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}



@app.get("/predict")

def predict(timestamp):
    df = pd.read_csv('../api_predict_df')
    df_ind = df.loc[df['timestamp'] == timestamp].index[0]
    X_predict = df.iloc[df_ind - 680:df_ind,2:]
    X_predict = np.array(X_predict).reshape(1, 680, 33)
    model = load_model('../initial_model')
    prediction = model.predict(X_predict)
    return {'prediction': prediction.tolist()}
