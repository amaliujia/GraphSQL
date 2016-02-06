from sql import *

def hello():
    print "HELLO WORD"

def file_to_table(db_instance, name="", data_path=""):
    lines = [line.rstrip('\n') for line in open(data_path)]
    cursor = db_instance.cursor()

    for line in lines:
        vertice = line.split(" ")
        i = insert_table(graph_temp, [int(vertice[0]), int(vertice[1])])
        cursor.execute(i)

    return

def ugraph(db_instance, graph_src, graph_dst):
    cursor = db_instance.cursor()

    s = create_ugraph(graph_src, graph_dst)
    cursor.execute(s)

def kcore(db_instance, data_path=""):
    cursor = db_instance.cursor()

    GRAPH_TABLE_TEST = "graph_temp"
    GRAPH_TABLE = "graph"
    GRAPH_SCHEMA = {"src_id":"INT", "dst_id":"INT"}

    g1 = create_table(GRAPH_TABLE, GRAPH_SCHEMA)
    g2 = create_table(GRAPH_TABLE_TEST, GRAPH_SCHEMA)
    cursor.execute(g1)
    cursor.execute(g2)

    # load data into table
    file_to_table(db_instance, GRAPH_TABLE_TEST, data_path)

    # create a undirected graph
    ugraph(GRAPH_TABLE_TEST, GRAPH_TABLE)


def main():
    lines = [line.rstrip('\n') for line in open("/Users/amaliujia/Documents/github/GraphSQL/unit_test_sets/kcore_1.txt")]

    for line in lines:
        vertice = line.split(" ")
        i = insert_table("a", [int(vertice[0]), int(vertice[1])])
        print i



if __name__ == "__main__":
    main()
