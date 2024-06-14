FROM python:3.12

RUN mkdir /betarget

WORKDIR /betarget

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

#CMD gunicorn backend.src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
