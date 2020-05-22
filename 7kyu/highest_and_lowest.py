
# In this assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):

    new_list = list(map(int, numbers.split()))
    max = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] > max:
            max = new_list[i]

    min = new_list[0]
    for i in range(len(new_list)):
        if new_list[i] < min:
            min = new_list[i]

    output = f'{max} {min}'
    return output

print(high_and_low("1 2 -3 4 5"))

