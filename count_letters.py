import re
def count_words(s):
    cleaned_string = re.sub(r'[^a-z]','', s.lower())
    dictionary = {}
    for char in cleaned_string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary