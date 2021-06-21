#!/usr/bin/python3

import mysql.connector
import sys,configparser         #config parser estrapola le credenziali di MariaDB

# Connect to MariaDB Platform

config = configparser.ConfigParser()
config.read('config.ini')

try:
    conn = mysql.connector.connect(
        user=config['mariaDB']['user'],
        password=config['mariaDB']['psw'],
        host=config['mariaDB']['host'],
        database=config['mariaDB']['db'])

except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


query = ('select Category from MotQuotes')


cur.execute(query)

myresult = cur.fetchall()

count = len(myresult)
print(count)

for x in myresult:
  print(x)

