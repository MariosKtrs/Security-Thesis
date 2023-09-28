# Use the official WordPress image as a base
FROM wordpress:php7.1-apache

# Set environment variables
ENV WORDPRESS_DB_HOST=db:3306
ENV WORDPRESS_DB_USER=root
ENV WORDPRESS_DB_PASSWORD=password
ENV WORDPRESS_DB_NAME=database

# Mount volumes
VOLUME /var/www/html
