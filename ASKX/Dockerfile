FROM ubuntu:22.04

#update the container
RUN apt-get update -y 


#install gdb to reverse-engineer the file
RUN apt-get install -y gdb

<<<<<<< HEAD
RUN apt-get install -y lib32z1 libseccomp-dev 
=======
RUN apt-get install -y lib32z1 libseccomp-dev
>>>>>>> 03f90aa2121dd3f075b9fbe5d8165abe68f9bbfb

#clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/challenge

COPY vulnerable/a.out /home/challenge

EXPOSE 1337

CMD ["tail", "-f", "/dev/null"]
