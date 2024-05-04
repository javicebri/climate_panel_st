def unique(lista):
    unique_list = []
    for x in lista:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list