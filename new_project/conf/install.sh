#!/usr/bin/env bash

INITIAL_DIR=$(pwd)
node -v >.nvmrc
NODE_VERSION=$(cat .nvmrc)
rm .nvmrc
echo "$INITIAL_DIR"

#create bash_profile file if not present
if ! [[ -f $HOME/.bash_profile ]]; then
  touch "$HOME"/.bash_profile
fi

if [[ ! -d "backend" ]] && [[ ! -d "frontend" ]]; then
  echo "This script should be run at the root of the new_project folder!"
  exit 1
fi


if [[ "$NODE_VERSION" == "" ]]
then
    echo "Unable to determine the version of NodeJS to install!"
    exit 1
else
    chown -R "$(whoami)" "$HOME/.nvm" | true

    #install NVM, Node, Node Automatic Version switcher
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash &&
    export NVM_DIR="$HOME/.nvm" &&
    # shellcheck disable=SC1073
    # shellcheck disable=SC1090
    [[ -s "$NVM_DIR/nvm.sh" ]] && \. "$NVM_DIR/nvm.sh" || ( echo "Error loading NVM " && exit 1 ) ; # This loads nvm

    if [[ -f $HOME/.bashrc ]]; then
   		# shellcheck disable=SC1090
   		source $HOME/.bashrc
    fi

    if [[ -f $HOME/.bash_profile ]]; then
   		# shellcheck disable=SC1090
   		source $HOME/.bash_profile
    fi
#    nvm install "$NODE_VERSION"
#    nvm use --delete-prefix "$NODE_VERSION" --silent

    echo "Installing Node Version $NODE_VERSION during install script!!"
    nvm install $NODE_VERSION &&
    nvm use --delete-prefix $NODE_VERSION --silent &&
    echo "loaded NVM."

    #clear npm cache
    npm cache clean --force

    #delete node_modules folder
    rm -rf node_modules
    rm -rf package-lock.json

    chown -R "$(whoami)" "$HOME/.nvm"

    #install preliminary dependencies
    npm i -g grunt && npm install gulp-cli -g && npm install bower -g && npm install pm2 -g && npm install -g npm-check-updates

    #install dependencies. Will also run bower install whenever needed
    npm install #this is needed when running npm install with sudo to install global modules

    #use grunt to put everything in place
    grunt
fi

# Want NVM to be loaded on every terminal you open? Add to ~/.bash_profile this:

#export NVM_DIR="$HOME/.nvm" &&
#[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

#

echo "Installing frontend app "
npm install

