#!/usr/bin/env bash
eval "$(conda shell.bash hook)"
conda activate archgraph
python ./src/Routes/routes.py
