#!/usr/bin/env sh

# Install WordPress.
wp core install \
  --title="VulnPress" \
  --admin_user="admin" \
  --admin_password="vU1n3r4bl3_p4ssw0rd" \
  --admin_email="test@gmail.com" \
  --url="http://127.0.0.1:8000/" \
