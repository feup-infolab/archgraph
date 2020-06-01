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

# preload graph
if [[ -z "$INIT_GRAPH" ]] ; then
    echo "Preload graph flag is not active, skipping tests"
elif [[ ! -f "$ROOT_DIR/.preloaded.txt" ]] || [[ "$FORCE_RELOAD_GRAPH" == "1" ]] ; then
    rm -f "$ROOT_DIR/.preloaded.txt"
    echo "Preload graph flag is active, loading graph through tests"
    coverage run -m unittest discover test
    echo "true" > "$ROOT_DIR/.preloaded.txt"
else
    echo "Preload graph flag is active but the database has already been initialized once. \
    To re-initialize, delete the $ROOT_DIR/.preloaded.txt file and run this script again, or \
    set the FORCE_RELOAD_GRAPH environment variable before re-running this script."
fi

echo "Starting archgraph server at $ROOT_DIR"
cd "$ROOT_DIR"

if [[ "$NEO4J_HOST" != "" ]]; then
    echo "Neo4j Server Host: $NEO4J_HOST"
else
    NEO4J_HOST="127.0.0.1"
fi

if [[ "$NEO4J_PORT" != "" ]]; then
    echo "Neo4j Server Port: $NEO4J_PORT"
else
    NEO4J_PORT="7687"
fi

if [[ "$MONGODB_HOST" != "" ]]; then
    echo "MongoDB Server Host: $MONGODB_HOST"
else
    MONGODB_HOST="127.0.0.1"
fi

if [[ "$MONGODB_PORT" != "" ]]; then
    echo "MongoDB Server Port: $MONGODB_PORT"
else
    MONGODB_PORT="27017"
fi

if [[ "$CUSTOM_HOST_FOR_SERVER_BIND" != "" ]]; then
    echo "Flask Server binding to host with address $CUSTOM_HOST_FOR_SERVER_BIND"
fi

## wait for servers to be active before running the application

./conf/wait-for-it.sh "$MONGODB_HOST:$MONGODB_PORT" --timeout=60 &
./conf/wait-for-it.sh "$NEO4J_HOST:$NEO4J_PORT" --timeout=60

wait

python "$ROOT_DIR/src/Routes/routes.py" &
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
