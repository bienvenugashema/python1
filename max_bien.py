
def max_bien(lst):
    lgst_num = lst[0]

    for item in lst:
        if item > lgst_num:
            lgst_num = item

    return lgst_num
