# Use a slim Python image as a parent image
FROM python:3.8-slim

# Set the working directory to /home
WORKDIR /home

# Create a "files" directory inside the container's home directory
RUN mkdir files

# Set the working directory to "files"
WORKDIR /home/files

# Copy the contents of the "Files" directory into the container at /home/Files
COPY files/ .

#Make the python file executable
RUN chmod +x CBC_encryption.txt ECB_encryption.txt

# Update the container
RUN apt-get -y update 

# install necessary packages
RUN pip install cryptography

# Clean up apt cache to reduce image size \
RUN apt-get clean && rm -rf /var/lib/apt/lists/* 

CMD ["tail", "-f", "/dev/null"]
