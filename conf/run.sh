#!/usr/bin/env bash
ROOT_DIR=$(pwd)

if [[ ! -f "README.md" ]] || [[ ! -f "requirements.txt" ]]; then
    echo "This script should be run at the root of the project!"
    exit 1
fi

#activate environment
source "./conf/activate.sh"

# activate nvm and use node v13
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
nvm use v13

python ./src/Routes/routes.py &
SERVER_PID=$!
cd "$ROOT_DIR/frontend" || ( echo "folder missing " && exit 1 )
yarn ng serve &
CLIENT_PID=$!
cd "$ROOT_DIR" || ( echo "folder missing " && exit 1 )

echo "Server running with pid $SERVER_PID and client running with pid $CLIENT_PID"

function kill_server_and_client {
    echo "Killing Python Server (PID $SERVER_PID) and Front end (PID $CLIENT_PID)...";
    kill -9 "$SERVER_PID"
    kill -9 "$CLIENT_PID"
}

trap kill_server_and_client INT

wait
