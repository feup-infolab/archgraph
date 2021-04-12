#!/usr/bin/env bash

INITIAL_DIR=$(pwd)
echo "$INITIAL_DIR"


if [[ ! -d "backend" ]] && [[ ! -d "frontend" ]]; then
  echo "This script should be run at the root of the new_project folder!"
  exit 1
fi


cd frontend || (echo "folder missing " && exit 1)

echo "starting up frontend App"
npm start &
CLIENT_PID=$!

echo "Server running with pid _____  and client running with pid $CLIENT_PID"

function kill_server_and_client() {
  echo "Killing Server (PID ___ ) and Front end (PID $CLIENT_PID)..."
  #kill -9 "$SERVER_PID"
  kill -9 "$CLIENT_PID"
}

trap kill_server_and_client INT

wait