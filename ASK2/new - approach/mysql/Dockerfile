# Use the official MySQL image as a base
FROM mysql:5.7

# Copy SQL initialization scripts
COPY ./database/ /docker-entrypoint-initdb.d

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=login_db
ENV MYSQL_ALLOW_EMPTY_PASSWORD=1

# Expose port
EXPOSE 3306
