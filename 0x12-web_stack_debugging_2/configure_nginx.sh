#!/bin/bash

# Install necessary packages
apt-get update
apt-get install -y nginx

# Modify nginx configuration
sed -i 's/user www-data;/user nginx;/g' /etc/nginx/nginx.conf
sed -i 's/# server_names_hash_bucket_size/server_names_hash_bucket_size/g' /etc/nginx/nginx.conf

# Create a backup of the default Nginx configuration file
mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup

# Create a new Nginx configuration file
cat << EOF > /etc/nginx/sites-available/default
server {
    listen 8080 default_server;
    listen [::]:8080 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }
}
EOF

# Restart Nginx service
service nginx restart
