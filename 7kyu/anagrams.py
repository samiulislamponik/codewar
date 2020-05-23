
def anagrams(word, words):

    check_list = sorted(list((word)))
    new_list = list(map(list,words))

    ultimate_list = []
    for i in new_list:

        if check_list == sorted(i):
            s = "".join(i)
            ultimate_list.append(s)

    if not ultimate_list:
        return []
    else:
        return ultimate_list

    
print(anagrams('abba', ['dsff', 'abcd', 'a', 'dada']))


