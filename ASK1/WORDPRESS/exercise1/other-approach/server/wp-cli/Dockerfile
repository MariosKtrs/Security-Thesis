# Use the official WordPress CLI image as a base
FROM wordpress:cli-php7.1

# Set environment variables
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV WORDPRESS_DB_HOST=db:3306
ENV WORDPRESS_DB_USER=root
ENV WORDPRESS_DB_PASSWORD=password

# Set the user
USER 33:33

# Mount volumes
VOLUME /var/www/html

# Specify the command to run (include the script contents)

CMD ["/bin/sh", "-c", \
  "echo 'Initiating account setup...'; \
   wp core download --path=/var/www/html && \
   wp core config --dbname=database --dbuser=root --dbpass=password --dbhost=db:3306 && \
   wp core install --url='http://127.0.0.1:8000/' --title='VulnPress' --admin_user='admin' --admin_password='vU1n3r4bl3_p4ssw0rd' --admin_email='test@gmail.com'"]
