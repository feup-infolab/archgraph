#!/bin/bash

ROOT_DIR=$(pwd)
echo "Running at $ROOT_DIR"

# maybe remove this later when conda is working correctly in path
# (this was not working on linux without re-exporting the folder to path?)

source "$HOME/.bash_profile" || source "$HOME/.profile" || ( echo "bash_profile missing" && exit 1 )
export PATH="$HOME/miniconda/bin":$PATH

if [[ ! -f "README.md" ]] || [[ ! -f "requirements.txt" ]]; then
    echo "This script should be run at the root of the project!"
    exit 1
fi

eval "$(conda shell.bash hook)"
conda activate archgraph
echo "Python interpreter is at: ---> $(which python) <---"