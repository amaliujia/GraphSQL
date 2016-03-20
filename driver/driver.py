from database import *
from sql import *
from graphlib import *
import sys
import time

db_instance = None


def main():
    global db_instance
    command = sys.argv[1]
    data = sys.argv[2]
    index = False
    composite_index = False
    clustering_index = False
    index = (sys.argv[3] == "True")
    composite_index = (sys.argv[4] == "True")
    clustering_index = (sys.argv[5] == "True")
    try:
        if db_instance == None:
            db_instance = db_connect()

        if command == "kcore":
          kcore(db_instance, data, index, composite_index, clustering_index)

        if command == "degreedist":
          degree_distribution(db_instance, data)
    except:
        print "Unexpected error:", sys.exc_info()
    finally:
      print command + " " + data + " " + " index " + str(index) + " composite_index " + str(composite_index) + "  clustering index " + str(clustering_index)
      if db_instance:
        db_disconnect(db_instance)

if __name__ == '__main__':
    main()
