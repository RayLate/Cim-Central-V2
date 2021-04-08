FROM python:3.9
LABEL maintainer="rming@micron.com"

#RUN apt-get update -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV HTTP_PROXY 'http://proxy-web.micron.com:80'
ENV HTTPS_PROXY 'http://proxy-web.micron.com:80'

COPY . .

# RUN chmod g+r -R sample-app/wsgi.py ./welcome

EXPOSE 8000
RUN python manage.py runserver
# CMD ["gunicorn", "-c", "guniconf.py", "sample-app.wsgi"]