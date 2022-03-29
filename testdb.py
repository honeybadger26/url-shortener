import MySQLdb
import sys

try:
    connect = MySQLdb.connect(
        host='db',
        database='urlshortener',
        user='user1',
        password='pword'
    )
    connect.close()
except:
    sys.exit(1)