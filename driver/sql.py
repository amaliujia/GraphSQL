
def drop_table_if_exist(name=""):
    return "DROP TABLE IF EXISTS %s" % (name);


def insert_table(name="", records=list(), schema={}):
    ret = "INSERT INTO %s VALUES(" % name
    content = ""
    for record in records:
        if len(content) != 0:
            content += ", "
        content += str(record)
    content += ")"
    return ret + content


def create_ugraph(src="", dst=""):
    ret = "INSERT INTO %s\n" % dst
    ret += "  SELECT src_id, dst_id FROM %s\n" % src
    ret += "  UNION\n"
    ret += "  SELECT dst_id AS src_id, src_id AS dst_id FROM %s" % src
    return ret


def select_from(name="", target="", condition=""):
    ret = "SELECT "
    if target != "":
        ret += "%s FROM %s" % (target, name)
    else:
        ret += "* FROM %s" % name
    if condition != "":
        ret += "\nWHERE %s" % condition
    return ret


def create_table(name="", schema={}):
    s1 = "CREATE TABLE %s(" % (name)
    s2 = ""
    for key, value in schema.iteritems():
        if len(s2) != 0:
            s2 += ", "
        s2 += str(key)
        s2 += " "
        s2 += str(value)
    s3 = ")"

    return  s1 + s2 + s3


def insert_out_degree(graph_name="", degree_name=""):
    ret = "INSERT INTO %s (id, degree)\n" % degree_name
    ret += graph_out_degree(graph_name)
    return ret


def graph_out_degree(name=""):
    ret = "SELECT A.src_id, count(*) AS out_degree\n"
    ret += " FROM %s AS A\n" % name
    ret += " GROUP BY A.src_id\n"
    ret += " ORDER BY A.src_id ASC"
    return ret


def graph_k_degree_top_one(name="", k=0):
    ret = "SELECT src_id, out_degree\n"
    ret += "  FROM (\n"
    ret += graph_out_degree(name)
    ret += "\n) AS N\n"
    ret += "WHERE N.out_degree < %d\n" % k
    ret += "ORDER BY N.out_degree ASC\n"
    ret += "LIMIT 1"
    return ret


def graph_delete_node(name="", id=0):
    request = "DELETE FROM %s\n" % name
    request += "WHERE src_id=%d\n" % id
    request += "OR\n"
    request += "dst_id=%d" % id
    return request


def creat_index(name="", col=""):
    request = "create index %s_%s on %s (%s)" % (name, col, name, col)
    return request

def create_clustered_index(name="", col=""):
    request = "CLUSTER %s USING %s_%s" % (name, name, col)
    return request

def creat_index_on_two_columns(name="", col="", col2=""):
    request = "create index %s_%s_%s on %s (%s, %s)" % (name, col, col2, name, col, col2)
    return request


def ugraph_insert_degree_distribution(dist_table="", graph=""):
    request = "INSERT INTO %s (degree, count)\n" % dist_table
    request += ugraph_degree_distriution(graph)
    return request


def graph_insert_degree_distribution(dist_table="", graph=""):
    request = "INSERT INTO %s (degree, count)\n" % dist_table
    request += ugraph_degree_distriution(graph)
    return request


def graph_degree_distriution(name=""):
    request = "SELECT degree, count(*)\n"
    request += "FROM (\n"
    request += "  SELECT count(*) AS degree\n"
    request += "  FROM %s AS A\n" % name
    request += "  GROUP BY A.dst_id\n"
    request += "  UNION ALL\n"
    request += "  SELECT count(*) AS Degree\n"
    request += "  FROM %s AS A\n" % name
    request += "  GROUP BY A.src_id\n"
    request += ") AS degree_table\n"
    request += "GROUP BY degree\n"
    request += "ORDER BY degree ASC"
    return request


def ugraph_degree_distriution(name=""):
    request = "SELECT degree, count(*)\n"
    request += "FROM (\n"
    request += "  SELECT count(*) AS degree\n"
    request += "  FROM %s AS A\n" % name
    request += "  GROUP BY A.dst_id\n"
    request += ") AS degree_table\n"
    request += "GROUP BY degree\n"
    request += "ORDER BY degree ASC"
    return request


def main():
    print create_table("TEST", {"id":"INT", "value":"REAL"})
    print drop_table_if_exist("TEST")
    print insert_table("TEST", [1, 0.1])
    print create_ugraph("SRC", "DST")
    print "\n"
    print graph_out_degree("TEST")
    print "\n"
    print graph_k_degree_top_one("GRAPH", 2)
    print "\n"
    print graph_delete_node("GRAPH", 1)
    print "\n"
    print creat_index("GRAPH", "COL")
    print "\n"
    print insert_out_degree("GRAPH", "DEGREE")
    print "\n"
    print select_from("Table", "serc_id", "dest = 5")
    print "\n"
    print ugraph_insert_degree_distribution("degree_distr", "graph")

if __name__ == '__main__':
    main()
