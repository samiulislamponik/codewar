
def high(x):
    new_list = x.split()
    new_list.append("0")
    char_list = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    arr = []
    j = 0
    while(j < len(new_list)):

        if new_list.index(new_list[j]) > 0:
            arr.append(sum)

        sum = 0
        for i in new_list[j]:
            for key in char_list:
                if i == key:
                    sum = sum + char_list[key]

        j  += 1

    value = arr.index(max(arr))
    for item in new_list:
        if new_list.index(item) == value:
            return item


print(high('man i need a taxi up to ubud'))