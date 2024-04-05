# #!/bin/bash

# # MySQL credentials
username="root"
password="mK3CuqT8oKBsgmop5eap"
database="Demo"
host="ems-db.cbew84swqjs6.eu-north-1.rds.amazonaws.com"

python3 Demo.py
# # Path to the SQL file
# sql_file="/home/rishi/Desktop/Working_Projects/EMS-DB-Server/laravel_demo.sql"


sql_file="/home/ubuntu/EMS-Db_script/DeployScript/ems.sql"

mysql -u "$username" -p"$password" -h "$host" "$database" <<EOF
drop database Demo;
create database Demo;
EOF

echo "Drop successful"

mysql -u"$username" -p"$password" -h "$host" "$database" < "$sql_file"

echo "Imported Successfully!"
