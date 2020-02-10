#!/bin/bash

# clean dependencies
rm -rf backend/env/bin
rm -rf backend/env/include
rm -rf backend/env/lib
rm -rf backend/env/man

brew install python3 || brew upgrade python3

# install venv
python3 -m venv env
# activate venv
source env/bin/activate
# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
# upgrade pip to latest version
pip install --upgrade pip
# (optional) install any requirements of your current app in this venv
pip install -r requirements.txt