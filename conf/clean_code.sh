#!/usr/bin/env bash

ROOT_DIR=$(pwd)

if [ ! -f "$ROOT_DIR/README.md" ] || [ ! -f "$ROOT_DIR/requirements.txt" ]; then
    echo "This script should be run at the root of the project!"
    exit 1
fi

#activate environment
source "./conf/activate.sh"

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
