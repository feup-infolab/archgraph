#!/usr/bin/env bash


if psql -l|awk '{print $1}'|grep -w dbs ; then
  echo "Database exists already."
  exit
fi
  echo "Database exists aasa."
