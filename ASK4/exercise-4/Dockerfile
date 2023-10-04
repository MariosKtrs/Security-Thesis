FROM php:apache
COPY index.php styles.css bg.jpg /var/www/html/
RUN mkdir -p /home/secret/flag.txt
COPY flag.txt /home/secret/
EXPOSE 80
