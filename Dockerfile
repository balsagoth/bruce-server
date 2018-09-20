FROM kennethreitz/pipenv

COPY . /app
CMD gunicorn bruceguts.http:app -k gevent -b 0.0.0.0:80
