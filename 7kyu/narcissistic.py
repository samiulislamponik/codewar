
def narcissistic(value):
    if value == int(value):
        new_str = str(value)
        l = len(new_str)
        sum = 0
        for i in new_str:
            sum += int(i)**l

        if value == sum:
            return True
        else:
            return False

    else:

        return "For text strings or other invalid inputs is not required, only valid integers will be passed into the function."


print(narcissistic("32"))


