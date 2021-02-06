!/bin/sh
rm -rf /etc/letsencrypt
certbot certonly --webroot -w /usr/share/nginx/html --email $REGISTER_EMAIL --non-interactive --agree-tos --cert-name generatedcert --domains $DOMAINS --staging
nginx -s reload