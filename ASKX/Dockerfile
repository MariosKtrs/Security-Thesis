FROM ubuntu:22.04

#update the container
RUN apt-get update -y 

#install gdb to reverse-engineer the file
RUN apt-get install -y gdb

#install some 32bit libraries
RUN apt-get install -y lib32z1 libseccomp-dev

#clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/challenge

COPY vulnerable/a.out /home/challenge

EXPOSE 1337

CMD ["tail", "-f", "/dev/null"]
