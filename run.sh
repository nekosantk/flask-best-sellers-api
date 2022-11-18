#!/bin/bash
if [ "$1" = 'test' ]; then
  poetry run pytest -s --verbose
else
  poetry run flask run
fi