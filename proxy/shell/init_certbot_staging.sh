#!/bin/ash
rm -rf /etc/letsencrypt/live
certbot certonly --webroot -w /usr/share/nginx/html --email $REGISTER_EMAIL --non-interactive --agree-tos --cert-name generatedcert --domains $DOMAINS --staging
nginx -s reload