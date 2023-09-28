# Use the official MySQL image as a base
FROM mysql:5.7

# Copy SQL initialization scripts
COPY ./database/user_info.sql /docker-entrypoint-initdb.d/user_info.sql
COPY ./database/database.sql /docker-entrypoint-initdb.d/database.sql

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=database
ENV MYSQL_ALLOW_EMPTY_PASSWORD=no

# Expose port
EXPOSE 3306
