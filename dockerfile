FROM python:3.9-slim
LABEL maintainer="rming@micron.com"

#RUN apt-get update -y
COPY /app .

WORKDIR /app
RUN dir
# COPY . .
# # COPY pip.ini /etc/pip.conf

# RUN file="$(ls -1 /)" && echo $file

# ENV NO_PROXY .micron.com
# ENV SSL_VERIFY False
# ENV REQUESTS_CA_BUNDLE micronCAchain.pem
# COPY /app/requirements.txt .
# RUN pip install -r requirements.txt

# ENV HTTP_PROXY 'http://proxy-web.micron.com:80'
# ENV HTTPS_PROXY 'https://proxy-web.micron.com:80'

# COPY . .

# # RUN chmod g+r -R sample-app/wsgi.py ./welcome

# EXPOSE 8000
# RUN python manage.py runserver
# # CMD ["gunicorn", "-c", "guniconf.py", "sample-app.wsgi"]