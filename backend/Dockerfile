FROM python:3.12

RUN mkdir /betarget_backend

WORKDIR /betarget_backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh