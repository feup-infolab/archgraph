#!/usr/bin/env bash

ROOT_DIR=$(pwd)
echo "Installing frontend dependencies at $ROOT_DIR"

ARCHGRAPH_ENV="archgraph"
PYTHON27_ENV="nodegyp-python27"

# install nodejs and yarn
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash

# activate nvm
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm

#install nodejs
nvm install v10
nvm use v10

# install frontend stuff
cd "$ROOT_DIR/frontend"
npm install -g npm@6.14.4
npm config set python "$PYTHON27_PATH"
npm install
echo "Current directory: $(pwd)"
ls -la
cd -
