FROM ubuntu:latest

#update the container
RUN apt-get update -y 

#install gdb to reverse-engineer the file
RUN apt-get install -y gdb

RUN apt-get install -y lib32z1 libseccomp-dev
RUN apt-get install -y nano

#clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /home/challenge

COPY vulnerable/ /home/challenge

EXPOSE 1337

CMD ["tail", "-f", "/dev/null"]
