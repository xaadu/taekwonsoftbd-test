FROM nginx:1.19.6-alpine
EXPOSE 80 443

ENV REGISTER_EMAIL xaadu1@gmail.com
ENV DOMAINS www.thexstech.tk,thexstech.tk

COPY webconfig/nginx.conf /etc/nginx/nginx.conf
COPY webconfig/dummy_fullchain.pem /etc/letsencrypt/live/generatedcert/fullchain.pem
COPY webconfig/dummy_privkey.pem /etc/letsencrypt/live/generatedcert/privkey.pem

COPY shell/init_certbot.sh /home/init_certbot.sh
COPY shell/init_certbot_staging.sh /home/init_certbot_staging.sh
COPY shell/nginx_start.sh /home/nginx_start.sh

COPY ./uwsgi_params /etc/nginx/uwsgi_params

RUN apk update \
    && apk add certbot \
    && echo '0 0,12 * * * certbot renew --post-hook "nginx -s reload"' > /etc/crontabs/root \
    && dos2unix /home/init_certbot.sh \
    && dos2unix /home/init_certbot_staging.sh \
    && dos2unix /home/nginx_start.sh \
    && chmod +x /home/init_certbot.sh \
    && chmod +x /home/init_certbot_staging.sh \
    && chmod +x /home/nginx_start.sh

CMD ["/home/nginx_start.sh"]