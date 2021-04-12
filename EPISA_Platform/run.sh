
docker exec -it myfuseki bash
apt-get update
apt-get install -y --no-install-recommends procps
exit
docker start myfuseki