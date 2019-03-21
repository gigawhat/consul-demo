FROM consul:latest

RUN apk add --update supervisor python3 && \
    pip3 install flask

ADD rootfs /

ENTRYPOINT ["/usr/bin/supervisord","-n","-c","/etc/supervisord.conf"]
