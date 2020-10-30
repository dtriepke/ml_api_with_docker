FROM continuumio/anaconda3
EXPOSE 8000
RUN apt-get update && apt-get install -y apache2 \
    apache2-dev \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/flask_api_predict/
COPY ./main /var/www/flask_api_predict/
COPY ./wsgi.py /var/www/flask_api_predict/wsgi.py
RUN pip install -r requirement.txt
RUN /opt/conda/bin/mod_wsgi-express install-module
RUN mod_wsgi-express start-server wsgi.py --port=8000 \
    --user www-data --group www-data \
    --server-root=/etc/mod_wsgi-express-80 \
    --locale=en_US.UTF-8
CMD /etc/mod_wsgi-express-80/apachectl start -D FOREGROUND