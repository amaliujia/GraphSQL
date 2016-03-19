from database import *
from sql import *
from graphlib import *
import sys
import time

db_instance = None


def main():
    global db_instance
    command = sys.argv[1]
    try:
        if db_instance == None:
            db_instance = db_connect()

        if command == "kcore":
          kcore(db_instance, sys.argv[2])

        if command == "degreedist":
          degree_distribution(db_instance, sys.argv[2])
    except:
        print "Unexpected error:", sys.exc_info()
    finally: 
      if db_instance:
            db_disconnect(db_instance)

if __name__ == '__main__':
    main()
