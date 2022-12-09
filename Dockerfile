FROM python:3.10.5
COPY . proyecto
WORKDIR /proyecto
RUN pip install -r requirements.txt
ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload