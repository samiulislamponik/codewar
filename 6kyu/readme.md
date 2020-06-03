## Formatting Details:

- First Problem Name with my solution file link.
- Alternative code or Best Practice code.
- Concept That are Used.
- Problem link
- And It will be continued untile new Rank up.

# Problems Discussion Starts From Here:
** Here I am adding those problems wich I have solved in codewar and it's randomly pickup **


## [The Hashtag Generator](https://github.com/samiulislamponik/codewar/blob/master/6kyu/Hashtag_generator.py 'Problem-1')

```python
Solve1:

def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
  
 Solve2:
 
 def generate_hashtag(s): 
 
 return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False


```

` Here strip(), title(), and replace() concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/52449b062fb80683ec000024/python 'Codewar Problem')



## [Highest Scoring Word](https://github.com/samiulislamponik/codewar/blob/master/6kyu/Highest_scoring_word.py 'Problem-2')

```python
Solve1:

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

  
 Solve2:
 
 def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]  # all char value in ascci start from 97. like a=97, b=98 etc.
        list.append(scores)
    return words[list.index(max(list))]

```

` Here ord(), split(), max(), sum(), index() and lamda expresion concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python 'Codewar Problem')




## [RGB To Hex](https://github.com/samiulislamponik/codewar/blob/master/6kyu/RGB_To_Hex.py 'Problem-3')

```python
Solve1:

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

  
 Solve2:
 
 def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num

def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))

```

` Here max(), min(), format() and lamda expresion concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/513e08acc600c94f01000001/python 'Codewar Problem')





## [Permutations](https://github.com/samiulislamponik/codewar/blob/master/6kyu/Permutations.py  'Problem-4')

```python
Solve:

import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


```

` Here permutations(), join() and set() concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/5254ca2719453dcc0b00027d/python 'Codewar Problem')






