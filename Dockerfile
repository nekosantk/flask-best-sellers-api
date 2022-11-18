FROM python:3.10-slim
RUN apt-get update && apt-get install --no-install-recommends -y curl build-essential
RUN set -xe
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"
RUN poetry --version
COPY poetry.lock pyproject.toml ./
WORKDIR app
COPY . .
RUN poetry install
EXPOSE 5000
RUN chmod 755 ./run.sh
RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]
CMD [""]