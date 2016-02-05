import psycopg2
import sys
from param import *

def db_connect():
    config_string = "host='/tmp' dbname=%s user=%s port=%d" % (DB, DB_USER, DB_PORT)
    instance = psycopg2.connect(config_string)
    print "Connected To Database"
    return instance

def db_disconnect(instance):
    instance.close()
    print "Disconnected From Database"
