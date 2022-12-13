#!/usr/bin/env sh

# Install WordPress.
wp core install \
  --title="VulnPress" \
  --admin_user="admin" \
  --admin_password="12345" \
  --admin_email="katsarosm47@gmail.com" \
  --url="http://127.0.0.1:8000/" \
  --skip-email
  
wp plugin install wp-stats-manager --version=5.6 --activate --allow-root
