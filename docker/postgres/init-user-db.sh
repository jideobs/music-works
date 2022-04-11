#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER music_db_user WITH PASSWORD 'password' CREATEDB;
    CREATE DATABASE music;
    GRANT ALL PRIVILEGES ON DATABASE music TO music_db_user;
EOSQL
