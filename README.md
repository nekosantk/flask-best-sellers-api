# Coding Task BE: Top Sellers
```
Service that has 2 endpoints for fetching the top sales people overall and for a specific year.

http://{container_ip}:5000/api/v1/sellers/top
http://{container_ip}:5000/api/v1/sellers/{year}/top
```
# Docker (Normal)
```
docker pull nekosantk/coding_task_be:latest
docker run nekosantk/coding_task_be:latest
```
# Docker (Tests)
```
docker pull nekosantk/coding_task_be:lates
docker run nekosantk/coding_task_be:latest test
```
# Installation
```
apt-get update && apt-get install --no-install-recommends -y curl build-essential

curl -sSL https://install.python-poetry.org | python3 -

git clone git@github.com:nekosantk/coding_task_be.git

cd coding_task_be

poetry install

poetry run flask run
```
# Running server
```
poetry run flask run
```
# Running tests
```
poetry run pytest -s --verbose
```
