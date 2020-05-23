def sum_dig_pow(a, b):
    arr = []
    for number in range(a, b+1):

        j = 1
        sum = 0
        for i in str(number):
            sum = sum + int(i)**j

            j+=1
        if sum == number:
            arr.append(sum)

        number += 1

    return arr




print(sum_dig_pow(89, 135))