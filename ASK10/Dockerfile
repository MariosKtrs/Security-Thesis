FROM ubuntu:trusty

# Install necessary packages
RUN apt-get update && \
    apt-get install -y wget build-essential libssl-dev libpcre3-dev nodejs npm

# Download and build OpenSSL
ADD https://www.openssl.org/source/old/1.0.1/openssl-1.0.1f.tar.gz /builddir/
WORKDIR /builddir/
RUN tar xf openssl-1.0.1f.tar.gz

WORKDIR /builddir/openssl-1.0.1f
RUN ./config && make && make install_sw

# Download and build Nginx with OpenSSL
ADD https://nginx.org/download/nginx-1.10.2.tar.gz /builddir/
WORKDIR /builddir/
RUN tar xf nginx-1.10.2.tar.gz

WORKDIR /builddir/nginx-1.10.2
RUN ./configure --with-http_ssl_module --prefix=/usr/local/nginx/ \
    --without-http_gzip_module --with-openssl=/builddir/openssl-1.0.1f \
    --without-pcre --with-threads --without-http_rewrite_module && make && make install

# Set up HTML and JS app
RUN mkdir /workdir/
WORKDIR /workdir/
RUN mkdir certs
RUN /usr/local/ssl/bin/openssl req -x509 -newkey rsa:2048 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes -subj "/C=GR/ST=Attica/L=foo/O=UC3M/OU=SSE/CN=poc.heartbleed.sse.uc3m.bar"
ADD /app/login.html /workdir/html/
ADD /app/index.html /workdir/html/
ADD /app/app.js /workdir/
ADD /app/package.json /workdir/

# Install Node.js dependencies
RUN npm config set strict-ssl false
RUN npm config set registry http://registry.npmjs.org/ && \
    npm install

RUN npm install body-parser
RUN npm install cookie-parser
RUN apt-get install -y nmap
# Configure Nginx for serving HTML and JS app and proxying to Node.js
ADD nginx.conf /usr/local/nginx/conf/nginx.conf
ENV PATH="/usr/local/nginx/sbin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ssl/bin:${PATH}"
RUN apt-get install -y supervisor
ADD /app/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 80 443
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]]

