#!/usr/bin/env bash

INITIAL_DIR=$(pwd)
echo "$INITIAL_DIR"


if [[ ! -d "backendnode" ]]; then
  echo "This script should be run at the root of the new_project folder!"
  exit 1
fi

# shellcheck disable=SC2030
(npm run start:prod --prefix backendnode & SERVER_PID=$! || (echo "folder missing " && exit 1)) & npm run start & CLIENT_PID=$!
# shellcheck disable=SC2031
echo "Server running with pid $SERVER_PID and client running with pid $CLIENT_PID"
