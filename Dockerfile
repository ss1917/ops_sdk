FROM python:3.6-slim-stretch

ENV LANG en_US.UTF-8

ENV TZ Asia/Shanghai

COPY hack/sources.list /etc/apt/sources.list

# 内网缓存
#COPY hack/apt.conf /etc/apt/apt.conf

COPY . /tmp/

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y apt-transport-https ca-certificates procps curl net-tools git supervisor gcc make zlib1g-dev gnupg2 vim nano  \
    && curl https://mirrors.xtom.com/sb/nginx/public.key | apt-key add - \
    && echo "deb https://mirrors.xtom.com/sb/nginx/ stretch main" > /etc/apt/sources.list.d/sb-nginx.list \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y nginx \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install -U /tmp/ -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && rm -rf /tmp/* \
    && mkdir -p /var/www/

WORKDIR /var/www
