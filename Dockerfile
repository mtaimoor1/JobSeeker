FROM python:3.10

RUN apt update

ENV APP_HOME="/JobSeeker/"

RUN mkdir -p "${APP_HOME}"

WORKDIR ${APP_HOME}

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY . .

RUN export PYTHONPATH=${APP_HOME}

ENV aws_access_key="${aws_access_key}"

ENV aws_secret_key="${aws_secret_key}"

CMD ["uvicorn", "pipeline_api.main:app", "--host", "0.0.0.0", "--port", "80"]