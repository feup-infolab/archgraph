#!/usr/bin/env bash
ROOT_DIR=$(pwd)
echo "Running at $ROOT_DIR"

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
