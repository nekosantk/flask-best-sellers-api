FROM python:3.10-slim
RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential
RUN set -xe
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry --version
COPY poetry.lock pyproject.toml ./
WORKDIR app
COPY . .
ENV role=dev
RUN poetry install
EXPOSE 5000
CMD [ "poetry", "run", "python", "-m", "flask", "run", "--host=0.0.0.0" ]