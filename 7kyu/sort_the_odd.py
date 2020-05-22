


"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.
Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

"""


def sort_array(source_array):

    even_arr = []   # Here I am adding just even number from main list to this list.
    even_arr_index = [] # And this list containing index of those even number.
    odd_arr = [] # Here I am adding just odd number from main list to this list.

    for i in  source_array:
        if  i % 2 == 0 or i == 0:
            even_arr.append(i)
            even_arr_index.append( source_array.index(i))
        else:
            odd_arr.append(i)

    new_list = sorted(odd_arr)

    for i in range(len(even_arr)):

        new_list.insert(even_arr_index[i], even_arr[i])

    return new_list


print(sort_array([5, 3, 2, 8, 1, 4]))


