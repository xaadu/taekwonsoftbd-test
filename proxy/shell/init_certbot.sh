!/bin/sh
rm -rf /etc/letsencrypt/live/generatedcert
certbot certonly --webroot -w /usr/share/nginx/html --email $REGISTER_EMAIL --non-interactive --agree-tos --cert-name generatedcert --domains $DOMAINS
nginx -s reload