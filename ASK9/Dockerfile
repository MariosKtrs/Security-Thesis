FROM ubuntu:22.04

# Update the container
RUN apt-get update -y 

# Install gdb to reverse-engineer the file
RUN apt-get install -y gdb


# Install some 32bit libraries
RUN apt-get install -y lib32z1 libseccomp-dev

# Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/challenge

COPY vulnerable/vuln /home/challenge

WORKDIR /home/challenge

# Container runs at port 1337
EXPOSE 1337

# Keep the container alive using an empty command
CMD ["tail", "-f", "/dev/null"]
