#!/bin/bash
set -ex

# sleep 60

# --
# Poetry v.
# --
source /app/poetry-venv/bin/activate
cd /app/FN-Basic-Services

# --
# Wating for ES
./wait_for_es.sh $ES_HOST

poetry run uvicorn main:app --host=0.0.0.0 --port=8888 --workers 4