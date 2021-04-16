CREATE USER bitbucket WITH PASSWORD 'bitbucket' CREATEDB;
CREATE DATABASE bitbucket
    WITH 
    OWNER = bitbucket
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
