FROM python:3.9-slim
LABEL maintainer="rming@micron.com"
 
COPY . .
COPY pip.ini /etc/pip.conf
# RUN /bin/bash --login -c "ls"
 
ENV NO_PROXY .micron.com
ENV SSL_VERIFY /micronCAchain.pem
ENV REQUESTS_CA_BUNDLE /micronCAchain.pem
ENV HTTP_PROXY 'http://proxy-web.micron.com:80'
ENV HTTPS_PROXY 'http://proxy-web.micron.com:80'
 
WORKDIR /app
 

# RUN /bin/bash --login -c "ls"
 
RUN pip install --no-cache-dir -r requirements.txt
 
EXPOSE 8000
 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]