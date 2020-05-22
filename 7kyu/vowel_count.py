# Count the vowels into a string.

def getCount(inputStr):
    count = 0
    count = inputStr.count("a") + inputStr.count("e") + inputStr.count("i") + inputStr.count("o") + inputStr.count("u")
    return count


print(getCount("abcdeeiuf"))


