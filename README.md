# Summary
Sandbox for testing consul features (templates, etc) using docker.

The compose file spins up the consul server, a backend service named whoami, and a frontend service named bar.


# Running
* Build containers - `docker-compose build`
* Start containers - `docker-compose up -d`
* Consul server ui - http://localhost:8500
* Frontend ui - http://localhost:9090
* Watch request - `watch -d -n 1 curl -s http://localhost:9090/whoami`
* Watch frontend (nginx) config - `watch -n 1 docker-compose exec bar cat /etc/nginx/conf.d/default.conf`
* Scale up the whoami service - `docker-compose scale whoami=3`
* Stop containers - `docker-compose down`
