# Use a slim Python image as a parent image
FROM python:3.8-slim

# Set the working directory to /home
WORKDIR /home

# Create a "Files" directory inside the container's home directory
RUN mkdir Files

# Set the working directory to "Files"
WORKDIR /home/Files

# Copy the contents of the "Files" directory into the container at /home/Files
COPY Files/ .

#Make all files that end with .py executable
RUN find . -type f -name "*.py" -exec chmod +x {} \;

# Update the container
RUN apt-get -y update 

# Clean up apt cache to reduce image size \
RUN apt-get clean && rm -rf /var/lib/apt/lists/* 

CMD ["tail", "-f", "/dev/null"]
