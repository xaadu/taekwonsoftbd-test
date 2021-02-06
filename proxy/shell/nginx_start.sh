#!/bin/sh
if [ "$CERTBOT_MODE" = "PROD" ]
then
    echo "Starting certbot in PROD mode"
    sleep 5 && /home/init_certbot.sh &
    crond
elif [ "$CERTBOT_MODE" = "STAGING" ]
then
    echo "Starting certbot in STAGING mode"
    sleep 5 && /home/init_certbot_staging.sh &
    crond
else
    echo "Starting certbot in disabled mode"
fi
nginx -g "daemon off;"