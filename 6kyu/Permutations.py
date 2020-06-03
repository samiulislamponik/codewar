
def permutations(string):

    from itertools import permutations

    combination = permutations(string)
    li = []
    for i in combination:

        s = "".join(i)
        li.append(s)
    new_li = set(li)
    return list(new_li)


print(permutations('aabb'))



