#!/bin/bash

brew cask install miniconda || brew cask upgrade miniconda
conda create -y -n archgraph python=3.7 anaconda
conda activate archgraph
conda init
source ~/.bash_profile

# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
# upgrade pip to latest version
pip install --upgrade pip
# (optional) install any requirements of your current app in this venv
pip install -r requirements.txt
# Get location of python interpreter
echo "Python is at: ---> $(which python) <---"

exit 0


# old script below, before using conda

## clean dependencies
#rm -rf backend/env/bin
#rm -rf backend/env/include
#rm -rf backend/env/lib
#rm -rf backend/env/man
#
#brew install openssl
#brew link openssl --force
#brew uninstall python
#brew install python3 --with-brewed-openssl || brew upgrade python3 --with-brewed-openssl
#
##brew install python3 || brew upgrade python3
#
#brew link python
#
#brew install zlib
#export LDFLAGS="-L/usr/local/opt/zlib/lib"
#export CPPFLAGS="-I/usr/local/opt/zlib/include"
#
## install venv
#python -m venv env ||
## activate venv
#source env/bin/activate
## install pip
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py
## upgrade pip to latest version
#pip install --upgrade pip
## (optional) install any requirements of your current app in this venv
#pip install -r requirements.txt
