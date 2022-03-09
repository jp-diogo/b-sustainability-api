#FROM python:3
#COPY predict.py /predict.py
#COPY requirements.txt /requirements.txt
#COPY app /app
#RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.8.6-buster

COPY api /api
COPY initial_model /initial_model
COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
