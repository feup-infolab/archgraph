#!/usr/bin/env bash

# format code according to black code standard
# https://github.com/psf/black
black src

# Cleanup unused imports
# https://github.com/myint/autoflake
autoflake -r --in-place --remove-unused-variables --remove-all-unused-imports src/

# Sort imports
# https://github.com/timothycrosley/isort
isort -rc src/
