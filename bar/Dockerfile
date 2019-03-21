FROM consul:latest

RUN apk add --update nginx supervisor
RUN wget -O consul_template.tgz https://releases.hashicorp.com/consul-template/0.20.0/consul-template_0.20.0_linux_amd64.tgz && \
    tar -xzf consul_template.tgz && \
    mv consul-template /usr/local/bin && \
    rm -f consul_template.tgz

ADD rootfs /

ENTRYPOINT ["/usr/bin/supervisord","-n","-c","/etc/supervisord.conf"]
