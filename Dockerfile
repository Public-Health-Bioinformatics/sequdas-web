FROM php:7.2.1-apache
RUN apt-get update && apt-get install -y \
    unzip
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
RUN curl -L https://github.com/mudmin/UserSpice4/archive/master.zip --output /tmp/userspice.zip \
    && unzip /tmp/userspice.zip -d /tmp \
    && cp -r /tmp/UserSpice4-master /var/www/html/userspice \
    && chmod 666 /var/www/html/userspice/users/init.php
