FROM httpd:2.4
COPY ./Product-Landing-Page/ /usr/local/apache2/htdocs/
COPY vuln.sh /usr/local/apache2/cgi-bin
RUN sed -i '1c#!/usr/bin/perl' /usr/local/apache2/cgi-bin/printenv
RUN chmod +x /usr/local/apache2/cgi-bin/printenv
RUN chmod 755 /usr/local/apache2/cgi-bin/vuln.sh
CMD httpd-foreground -c "LoadModule cgid_module modules/mod_cgid.so"

