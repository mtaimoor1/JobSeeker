FROM python:3.10

RUN apt update

ENV APP_HOME="/JobSeeker/"

RUN mkdir -p "${APP_HOME}"

WORKDIR ${APP_HOME}

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY . .

RUN export PYTHONPATH=${APP_HOME}

WORKDIR pipeline_api/

CMD ["uvicorn", "main:app"]