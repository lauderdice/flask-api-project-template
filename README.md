# Introduction 

production start: 

    gunicorn main:app -w 1  -b 0.0.0.0:8888 
local dev start: 

    flask run

# Docker build

in top level directory: 

    docker build . -t application