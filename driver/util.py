
def tuple_list_to_dict(l=list()):
    ret = dict()
    for item in l:
        ret[item[0]] = item[1]

    return ret;


def main():
    print tuple_list_to_dict([(1,1), (2,1)])

if __name__ == "__main__":
    main()