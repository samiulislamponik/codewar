# Formatting Details:

- First Problem Name with file link.
- Alternative code or Best Practice code.
- New Concept Details.
- And It will be continued untile new Rank up.

# Problems Discussion Starts From Here:
** Here I am adding those problems wich I have solved in codewar and it's randomly pickup **

## [Vowel Count](https://github.com/samiulislamponik/codewar/blob/master/7kyu/vowel_count.py " Problem-1 ")

``` python

def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

```

` Here sum() is used for adding the count value.`


## [Highest and Lowest](https://github.com/samiulislamponik/codewar/blob/master/7kyu/highest_and_lowest.py " Problem-2 ")

```python

def high_and_low(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))

```

` Here max(), min() and formatted string concepts are being used.`



