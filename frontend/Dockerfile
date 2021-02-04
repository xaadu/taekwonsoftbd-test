FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf


USER root

RUN mkdir -p /var/www/html
RUN chmod 755 /var/www/html

COPY . /var/www/html

USER nginx
