#!/usr/bin/env bash
ROOT_DIR=$(pwd)
echo "Running at $ROOT_DIR"

# maybe remove this later when conda is working correctly in path
# (this was not working on linux without re-exporting the folder to path?)

source "$HOME/.bash_profile"
export PATH="$HOME/miniconda/bin":$PATH

# activate nvm and use node v13
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
nvm use v13

eval "$(conda shell.bash hook)"
conda activate archgraph
echo "Python interpreter is at: ---> $(which python) <---"
python ./src/Routes/routes.py &
SERVER_PID=$!
cd "$ROOT_DIR/frontend"
yarn ng serve &
CLIENT_PID=$!
cd "$ROOT_DIR"

echo "Server running with pid $SERVER_PID and client running with pid $CLIENT_PID"

function kill_server_and_client {
    echo "Killing Python Server (PID $SERVER_PID) and Front end (PID $CLIENT_PID)...";
    kill -9 "$SERVER_PID"
    kill -9 "$CLIENT_PID"
}

trap kill_server_and_client INT

wait
