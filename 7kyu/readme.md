## Formatting Details:

- First Problem Name with my solution file link.
- Alternative code or Best Practice code.
- New Concept Details.
- Problem link
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


## [Sort the odd](https://github.com/samiulislamponik/codewar/blob/master/7kyu/sort_the_odd.py " Problem-3 ")

```python

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]


```

` Here list comprehension, sorted() and pop() concepts are being used.`


## [Eureka](https://github.com/samiulislamponik/codewar/blob/master/7kyu/eureka.py "Problem-4")

```python

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))


```

` Here filter(), sum() and enumerate() concepts are being used. `

##### [Problem link](https://www.codewars.com/kata/5626b561280a42ecc50000d1/python "codewar problem")



## [My Anagrams](https://github.com/samiulislamponik/codewar/blob/master/7kyu/anagrams.py "Problem-5")

```python

Solve1:

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

Solve2:

def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)

```

` Here filter(), sorted(), list comprehension and lambda expression concepts are being used. `

##### [Problem link](https://www.codewars.com/kata/523a86aa4230ebb5420001e1/python "codewar problem")



## [Narcissistic Number](https://github.com/samiulislamponik/codewar/blob/master/7kyu/narcissistic.py "Problem-6")


```python

Solve1:

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

```

` Here sum() and len() concepts are being used. `

##### [Problem link](https://www.codewars.com/kata/5287e858c6b5a9678200083c/python "codewar problem")




## [Moving Zeros To The End](https://github.com/samiulislamponik/codewar/blob/master/7kyu/zeros.py "Problem-7")


```python

Solve1:

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
    
Solve2:

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)
    

```

` Here sorted()  and isinstance() and lamda expresion concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/52597aa56021e91c93000cb0/python "codewar problem")




                                                        **The End**





