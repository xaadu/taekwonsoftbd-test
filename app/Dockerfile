FROM python:3.9.1-alpine3.12

COPY ./requirements.txt ./requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk add zlib-dev jpeg-dev
RUN pip install -r requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN mkdir -p /staticfiles/static
RUN mkdir -p /staticfiles/media
COPY ./media /staticfiles/media

RUN adduser -D user

RUN chown -R user:user /staticfiles
RUN chmod -R 755 /staticfiles

RUN chown -R user:user /app
RUN chmod -R 755 /app

#RUN chmod -R 555 /static
USER user

#CMD [ "entrypoint.sh" ]
ENTRYPOINT python manage.py makemigrations \
    &&python manage.py migrate \
    &&python manage.py collectstatic --noinput \
    &&uwsgi --socket :8000 --master --enable-threads --module portfolio.wsgi
#&&python manage.py runserver 0.0.0.0:8000
