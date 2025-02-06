FROM python:3.12

WORKDIR /app
COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip3 install -U pip \
  & pip3 install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]