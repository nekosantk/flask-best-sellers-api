# Coding Task BE: Top Sellers
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
