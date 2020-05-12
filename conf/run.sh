#!/usr/bin/env bash
ROOT_DIR=$(pwd)

if [[ ! -f "README.md" ]] || [[ ! -f "requirements.txt" ]]; then
    echo "This script should be run at the root of the project!"
    exit 1
fi

#activate environment
ROOT_DIR=$(pwd)
echo "Running at $ROOT_DIR"

# maybe remove this later when conda is working correctly in path
# (this was not working on linux without re-exporting the folder to path?)

if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    # init conda cli
    source "$HOME/miniconda/etc/profile.d/conda.sh"
fi

conda init zsh &> /dev/null
source "$HOME/.zshrc" &> /dev/null
conda init bash &> /dev/null
source "$HOME/.bash_profile" &> /dev/null

if [[ ! -f "README.md" ]] || [[ ! -f "requirements.txt" ]]; then
    echo "This script should be run at the root of the project!"
    exit 1
fi

conda activate archgraph
echo "Python interpreter is at: ---> $(which python) <---"
echo "Pip is at: ---> $(which pip) <---"

# activate nvm and use node v13
export NVM_DIR="$([[ -z "${XDG_CONFIG_HOME-}" ]] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[[ -s "$NVM_DIR/nvm.sh" ]] && \. "$NVM_DIR/nvm.sh" # This loads nvm
nvm use v10

echo "Starting archgraph server at $ROOT_DIR"
cd "$ROOT_DIR"

python "$ROOT_DIR/src/Routes/routes.py" --neo4j="$NEO4J_CONNECTION_STRING" --mongodb="$MONGODB_CONNECTION_STRING" &
SERVER_PID=$!
cd "$ROOT_DIR/frontend" || ( echo "folder missing " && exit 1 )
if [[ "$RUN_IN_PRODUCTION" != "" ]] ; then
    echo "Running archgraph frontend in production mode."
    npm run start-prod &
else
    npm start &
fi

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
