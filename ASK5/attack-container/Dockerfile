FROM ubuntu:22.04
RUN mkdir -p /home/wordlist/
COPY wordlist/wordlist.txt /home/wordlist/
RUN apt-get update -y
RUN apt install -y gobuster curl
CMD ["tail", "-f", "/dev/null"] 
