#!/bin/sh

docker start fuseki
docker exec -it fuseki bash
#root@7fc3133f5863:/jena-fuseki
apt-get update && apt-get install -y --no-install-recommends procps && exit
docker stop fuseki
docker start fuseki