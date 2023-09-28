FROM php:apache

# Install the mysqli extension
RUN docker-php-ext-install mysqli

# Copy your website files to the container
COPY ./login/ /var/www/html/

EXPOSE 80
EXPOSE 443
