#!/bin/bash

set -x

mkdir -p ./logs/ ./data/

export PYTHONPATH=`pwd`

cd ./flow/

nohup python app.py 9932 3 >> ../logs/service.log 2>&1 &

