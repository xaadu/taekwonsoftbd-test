#FROM nginxinc/nginx-unprivileged:1-alpine
FROM ubuntu:20.04

COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /var/www/html
RUN chmod 755 /var/www/html

RUN apt-get update -y \
    && apt-get install nginx -y \
    && apt-get install python3-certbot-nginx -y \
    && apt-get clean

EXPOSE 80 443

STOPSIGNAL SIGTERM

#CMD ["nginx", "-g", "daemon off;"]

ENTRYPOINT nginx \
    && certbot --nginx -d thexstech.tk -d www.thexstech.tk -m xaadu1@gmail.com --no-redirect --agree-tos --no-eff-email --test-cert \
    && nginx -s stop \
    && nginx -g "daemon off;"
