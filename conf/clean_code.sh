#!/usr/bin/env bash

eval "$(conda shell.bash hook)"
conda activate archgraph
echo "Python interpreter is at: ---> $(which python) <---"

# fix code style issues using autopep8
# https://github.com/hhatto/autopep8
autopep8 --aggressive -r --in-place src

# format code according to black code standard
# https://github.com/psf/black
black src

# Cleanup unused imports
# https://github.com/myint/autoflake
autoflake -r --in-place --remove-unused-variables --remove-all-unused-imports src/

# Sort imports
# https://github.com/timothycrosley/isort
isort -rc src/
