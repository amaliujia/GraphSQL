from database import *
from sql import *
from graphlib import hello

db_instance = None


def main():
    global db_instance

    try:
        if db_instance == None:
            db_instance = db_connect()

        kcore(db_instance, "/Users/amaliujia/Documents/github/GraphSQL/unit_test_sets/kcore_1.txt")

        if db_instance:
            db_disconnect(db_instance)
    except:
        print "Unexpected error:", sys.exc_info()
        if db_instance:
            db_disconnect(db_instance)

if __name__ == '__main__':
    main()
