#!/usr/bin/env bash
# Script to initialize MySQL user and permissions
# Run this after MySQL service is started: devenv up

mysql -u root <<EOF
CREATE USER IF NOT EXISTS 'todoapp'@'localhost' IDENTIFIED BY 'todoapp';
GRANT ALL PRIVILEGES ON todoapp.* TO 'todoapp'@'localhost';
FLUSH PRIVILEGES;
EOF

echo "MySQL user 'todoapp' created and granted privileges on 'todoapp' database"

