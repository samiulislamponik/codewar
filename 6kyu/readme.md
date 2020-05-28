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
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


```

` Here split(), max(), sum(), index() and lamda expresion concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python 'Codewar Problem')



