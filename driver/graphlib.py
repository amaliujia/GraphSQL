from sql import *

def hello():
    print "HELLO WORD"

def file_to_table(db_instance, name="", data_path=""):
    lines = [line.rstrip('\n') for line in open(data_path)]
    cursor = db_instance.cursor()

    for line in lines:
        vertice = line.split(" ")
        i = insert_table(name, [int(vertice[0]), int(vertice[1])])
        cursor.execute(i)
        db_instance.commit()


    return

def ugraph(db_instance, graph_src, graph_dst):
    cursor = db_instance.cursor()

    s = create_ugraph(graph_src, graph_dst)
    cursor.execute(s)
    db_instance.commit()


def kcore(db_instance, data_path=""):
    cursor = db_instance.cursor()

    GRAPH_TABLE_TEST = "graph_temp"
    GRAPH_TABLE = "graph"
    GRAPH_SCHEMA = {"src_id":"INT", "dst_id":"INT"}

    g1 = create_table(GRAPH_TABLE, GRAPH_SCHEMA)
    g2 = create_table(GRAPH_TABLE_TEST, GRAPH_SCHEMA)
    # cursor.execute(g1)
    # db_instance.commit()
    # cursor.execute(g2)
    # db_instance.commit()

    # load data into table
    # file_to_table(db_instance, GRAPH_TABLE_TEST, data_path)

    # create a undirected graph
    ugraph(db_instance, GRAPH_TABLE_TEST, GRAPH_TABLE)

    # create coreness table
    CORENESS = "coreness"
    CORENESS_SCHEMA = {"id":"INT", "core":"INT"}
    g3 = create_table(CORENESS, CORENESS_SCHEMA)
    cursor.execute(g3)
    db_instance.commit()


    stop_query = "SELECT * FROM %s" % GRAPH_TABLE
    k = 2

    while(True):
        cursor.execute(stop_query)
        rows = db_instance.fetchall()
        # if empty graph table, then stop
        if len(rows) == 0:
            break






def main():
    lines = [line.rstrip('\n') for line in open("/Users/amaliujia/Documents/github/GraphSQL/unit_test_sets/kcore_1.txt")]

    for line in lines:
        vertice = line.split(" ")
        i = insert_table("a", [int(vertice[0]), int(vertice[1])])
        print i



if __name__ == "__main__":
    main()
