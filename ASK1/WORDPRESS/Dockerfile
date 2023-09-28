# Use a base image that contains Docker Compose and dependencies
FROM docker/compose:latest

# Set the working directory
WORKDIR /app

# Copy your application files into the image
COPY exercise1/wordpress-server/. .

RUN chmod +x bin/install.sh

# Define an entry point to run Docker Compose
ENTRYPOINT ["docker-compose","up","-d"]


