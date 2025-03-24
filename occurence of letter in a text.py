       
def remove_duplicate(lst):
    for i in set(lst):
        if lst.count(i) > 1:
            lst.remove(i)
    print(lst)            

remove_duplicate([1,2,3,4,5,3,7,2])            
