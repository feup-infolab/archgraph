#!/bin/bash
#dbName="db"
#query="SELECT count(*) FROM pg_database WHERE datname='$dbName'"
#databaseExists=$(psql -h localhost -U admin -c "$query" postgres)
## shellcheck disable=SC2206
#arrIN=(${databaseExists//count/ })
#
#if [[ ${arrIN[1]} -eq 0 ]]
#then
#  echo "Database doesn't exists"
#  createDatabase=$(psql -h localhost -U admin postgres -c "CREATE DATABASE $dbName")
#  echo "$createDatabase"
#
#  populateDatabase=$(psql -h localhost -U admin -d $dbName -p 5432 -a -f backendnode/config/populate.sql)
#  echo "$populateDatabase"
#else
#  echo "Database already exists"
#fi

npm run start & npm run start:prod --prefix backendnode
