#!/usr/bin/env bash
eval "$(conda shell.bash hook)"
conda activate archgraph
echo "Python interpreter is at: ---> $(which python) <---"
python ./src/Routes/routes.py
