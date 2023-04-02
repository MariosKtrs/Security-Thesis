FROM httpd:2.4 
COPY ./Product-Landing-Page/ /usr/local/apache2/htdocs/
COPY secret /usr/local/apache2/cgi-bin
RUN sed -i '1c#!/usr/bin/perl' /usr/local/apache2/cgi-bin/printenv
RUN chmod +x /usr/local/apache2/cgi-bin/printenv
RUN chmod 755 /usr/local/apache2/cgi-bin/secret
CMD httpd-foreground -c "LoadModule cgid_module modules/mod_cgid.so"
RUN apt-get update
RUN apt-get install -y build-essential wget libncurses5
# Install vulnerable bash 4.3 from package
RUN wget https://snapshot.debian.org/archive/debian/20140304T040604Z/pool/main/b/bash/bash_4.1-3_amd64.deb
RUN dpkg -i bash_4.1-3_amd64.deb
RUN mkdir -p /home/secret/flag.txt
COPY flag.txt /home/secret/
