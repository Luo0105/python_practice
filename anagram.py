def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2) #it's a list comparison, not a dictionary

def is_anagram1(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    count_s1 = {}
    count_s2 = {}
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1
    for char in s2:
        count_s2[char] = count_s2.get(char, 0) + 1
    return count_s1 == count_s2

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(f"Using sorted method: {is_anagram(s1, s2)}")
print(f"Using counting method: {is_anagram1(s1, s2)}")
