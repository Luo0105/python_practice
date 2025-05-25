def find_lonely_numbers(l):
    if len(l) < 2:
        return []
    lonely_numbers = []
    for num in l:
        if l.count(num+1) == 0 and l.count(num-1) == 0:
            lonely_numbers.append(num)

    return lonely_numbers

numbers = [1, 2, 2, 4, 6, 7]
lonely_numbers = find_lonely_numbers(numbers)
print("Lonely numbers:", lonely_numbers)