
def add(a_str):
    if a_str == "":
        return 0
    else:
        ret_num = 0
        a_list = a_str.split(",")
        for num in a_list:
            ret_num += int(num)
        return int(ret_num)
