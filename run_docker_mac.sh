#!/bin/bash

docker run --user $(id -u) --name orientdb -p 2424:2424 -p 2480:2480 \
    -v $(pwd)/volumes/orientdb/config:/orientdb/config \
    -v $(pwd)volumes/orientdb/databases:/orientdb/databases \
    -v $(pwd)volumes/orientdb/backup:/orientdb/backup \
    -e ORIENTDB_ROOT_PASSWORD=rootpwd \
    orientdb

