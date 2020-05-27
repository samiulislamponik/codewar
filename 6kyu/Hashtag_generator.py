
def generate_hashtag(s):
    if not s:
        return False
    else:
        x = s.split()
        new_list = []
        for i in x:
            new_list.append(i.capitalize())

        new_string = '#' + "".join(new_list)
        if len(new_string) > 140:
            return False
        else:
            return new_string


print(generate_hashtag(''))


