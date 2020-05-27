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

` Here [strip()](https://www.w3schools.com/python/ref_string_strip.asp) , title(), and replace() concepts are being used. `


##### [Problem link](https://www.codewars.com/kata/52449b062fb80683ec000024/python 'Codewar Problem')


