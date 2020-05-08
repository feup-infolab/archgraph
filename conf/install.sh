#!/bin/bash

ROOT_DIR=$(pwd)
echo "Running at $ROOT_DIR"

ARCHGRAPH_ENV="archgraph"
PYTHON27_ENV="nodegyp-python27"

if  [ "$(uname)" == "Darwin" ]; then
    # Do something under Mac OS X platform
    if [ $(conda > /dev/null) > /dev/null ]; then
        brew cask install miniconda || brew cask upgrade miniconda
    else
        echo "Miniconda already installed, continuing..."
    fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ] ; then
    if ! type conda &> /dev/null ; then
        # Do something under GNU/Linux platform
        rm -rf Miniconda3-latest-Linux-x86_64.sh
        wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
        chmod +x Miniconda3-latest-Linux-x86_64.sh
        ./Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda" || ./Miniconda3-latest-Linux-x86_64.sh -u -b -p "$HOME/miniconda"
        rm -rf Miniconda3-latest-Linux-x86_64.sh
    else
        echo "Miniconda already installed, continuing..."
    fi
fi

# run conda
if [ "$(uname)" == "Darwin" ]; then
      source "$HOME/.bash_profile"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    source "$HOME/.profile"
fi

if  [ "$(uname)" == "Darwin" ]; then
    # make conda binary available in path
    export PATH="$HOME/miniconda/bin":$PATH
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # init conda cli
    source "$HOME/miniconda/etc/profile.d/conda.sh"
fi

conda init bash
conda create --quiet -y -n "$PYTHON27_ENV" python=2.7 anaconda
conda activate "$PYTHON27_ENV"
PYTHON27_PATH=$(which python)
echo "Node-Gyp interpreter Python (2.7) is at: ---> ${PYTHON27_PATH} <---"

# create archgraph env
conda create --quiet -y -n "$ARCHGRAPH_ENV" python=3.7 anaconda
conda activate "$ARCHGRAPH_ENV"

# Get location of python interpreter
PYTHON_PATH=$(which python)
echo "Python interpreter is at: ---> ${PYTHON_PATH} <---"

# install pip
conda install pip -y --all --quiet
echo "Pip at: ---> $(which pip) <---"
# (optional) install any requirements of your current app in this venv
pip install -r "$ROOT_DIR/requirements.txt"


# install nodejs and yarn
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash

# activate nvm
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

#install nodejs
nvm install v10
nvm use v10

# install frontend stuff
cd frontend
npm install -g npm@latest
npm config set python "$PYTHON27_PATH"
npm install

# preload graph
if [ -z "$PRELOAD_GRAPH" ] ; then
    echo "Preload graph flag is not active, skipping tests"
else
    echo "Preload graph flag is active, loading graph through tests"
    coverage run -m unittest discover test || true
fi
