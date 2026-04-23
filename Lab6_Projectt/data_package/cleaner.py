def remove_duplicates(data_list):
    new_list = []
    for x in data_list:
        if x not in new_list:
            new_list.append(x)
    return new_list

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]