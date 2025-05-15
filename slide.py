def length_of_longest_substring(string):
    s = set()
    left = 0
    max_length = 0
    start_index = 0
    for right in range(len(string)):
        while string[right] in s:
            s.remove(string[left])
            left += 1
        s.add(string[right])
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_length = max(max_length, right - left + 1)
            start_index = left
    return start_index, max_length

def main():
    string = input("Enter a string: ")
    start_index, max_length = length_of_longest_substring(string)
    print(f"The longest substring without repeating characters is '{string[start_index:start_index + max_length]}' with length {max_length}.")

if __name__ == '__main__':
    main()