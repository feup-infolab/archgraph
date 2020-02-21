#!/bin/bash

ENV_NAME="archgraph"

if [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform
    brew cask install miniconda || brew cask upgrade miniconda
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # Do something under GNU/Linux platform
    rm -rf Miniconda3-latest-Linux-x86_64.sh
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda"
    rm -rf Miniconda3-latest-Linux-x86_64.sh
fi


# run conda
source "$HOME/.bash_profile"
export PATH="$HOME/miniconda/bin":$PATH
conda remove --name "$ENV_NAME" -y --all
conda create -y -n "$ENV_NAME" python=3.7 anaconda
conda activate "$ENV_NAME"
conda init bash

# install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
# upgrade pip to latest version
pip install --upgrade pip
# (optional) install any requirements of your current app in this venv
pip install -r requirements.txt
# Get location of python interpreter
echo "Python interpreter is at: ---> $(which python) <---"

# install nodejs and yarn
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash

# activate nvm
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

#install nodejs and yarn
nvm install v13
nvm use v13
npm install -g yarn


# run yarn install
cd frontend
yarn install
cd -

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
