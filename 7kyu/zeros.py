def move_zeros(array):

    array.sort(key=lambda item: item == 0 and not isinstance(item, bool))

    return array


print(move_zeros([0,1,None,2,False,1,0]))