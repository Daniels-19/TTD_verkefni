
def add(a_str):
    if a_str == "":
        return 0
    else:
        ret_num = 0
        another_list = []
        a_list = a_str.split(",")
        for i, num in enumerate(a_list):
            new_list = num.split("\n")
            a_list[i] = new_list
        for num in a_list:
            if "//" in num[0]:
                delimiter = num[0][-1]
                for i, num in enumerate(a_list):
                    new_list = num[1].split(delimiter)
                    another_list = new_list
            else:
                for value in num:
                    another_list.append(int(value))
        for num in another_list:
            if int(num) < 0 and str(ret_num).isdigit():
                ret_num = "Negatives not allowed:{}".format(str(num))
            elif int(num) < 0:
                ret_num += ",{}".format(str(num))
            elif int(num) <= 1000 and str(ret_num).isdigit():
                ret_num += int(num)
        return ret_num

if __name__ == "__main__":
    print(add("//X\n1X2"))