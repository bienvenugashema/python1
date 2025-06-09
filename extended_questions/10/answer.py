def pair_correspondings(lst1:list, list2:list) -> list:
    new_lst:list = []

    for tups in zip(lst1, list2) :
        new_lst.append(list(tups))
    return new_lst

print(pair_correspondings([1,2,3,4,5],[7,8,9,1,2]))    