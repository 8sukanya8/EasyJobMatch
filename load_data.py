def save_dict_to_file(dic, filename = 'dict.txt'):
        with open(filename, 'w') as f:
            for key in dic.keys():
                try:
                    value_str = ""
                    if(type(dic[key]) is tuple):
                        value_str = ascii(','.join(dic[key]))
                    else:
                        value_str = ascii(dic[key])
                    str = ascii("%s\n" + key + "," + value_str)
                    f.write(str)
                except UnicodeEncodeError as err:
                    raise UnicodeEncodeError(key)
            f.close()


def load_dict_from_file(filename):
    f = open(filename,'r')
    data=f.read()
    f.close()
    return eval(data)

def save_list_to_file(list, filename):
    with open(filename, 'w') as f:
        for item in list:
            f.write("%s\n" % item)
    f.close()

