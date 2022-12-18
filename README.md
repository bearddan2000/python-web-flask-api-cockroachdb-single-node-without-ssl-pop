# python-web-flask-api-cockroachdb-single-node-without-ssl-pop

## Description
Creates an api CRUD of `pop` for a flask project.

A python flask build, that connects to single node cluster
cockroach database without ssl.

If path is not found, will default to 404 error.

## Tech stack
- python
  - flask
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- cockroachdb

## Docker stack
- python:latest
- cockroachdb/cockroach:v19.2.4

## To run
`sudo ./install.sh -u`
- Endpoints
  - [Select all](http://localhost/pop)
  - Insert, Select, Update, Delete
    - /pop/<id>
- [node webui](http://localhost:8000)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [Cockroach setup](https://github.com/s0rg/cockroach-compose)
- [Python flask with cockroachdb](https://www.cockroachlabs.com/blog/building-application-cockroachdb-sqlalchemy-2/)
