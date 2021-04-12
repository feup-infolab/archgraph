#!/usr/bin/env bash

INITIAL_DIR=$(pwd)
echo "$INITIAL_DIR"


if [[ ! -d "backendnode" ]]; then
  echo "This script should be run at the root of the new_project folder!"
  exit 1
fi

npm run start & CLIENT_PID=$! & (npm run start:prod --prefix backendnode || (echo "folder missing " && exit 1))
# shellcheck disable=SC2031
echo "Server running with pid _____  and client running with pid $CLIENT_PID"
