FROM python

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip
RUN pip install -U setuptools wheel

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

RUN ["chmod", "+x", "/app/entrypoint.sh"]

ENTRYPOINT ["/app/entrypoint.sh"]
