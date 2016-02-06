
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


def main():
    print create_table("TEST", {"id":"INT", "value":"REAL"})
    print drop_table_if_exist("TEST")
    print insert_table("TEST", [1, 0.1])
    print create_ugraph("src", "dst")

if __name__ == '__main__':
    main()
