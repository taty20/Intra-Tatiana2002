my_list = ['Pierre', 'Julien', 'Anne', 'Marie','Lucien']

def quicksort(lst):
    if not lst:
        return []
    return (quicksort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            quicksort([x for x in lst[1:] if x >= lst[0]]))


print(quicksort(my_list))