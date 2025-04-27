def checkstring(word):
    word = word.lower().replace(" ", "")
    if len(word) == 0:
        print("The string is empty.")
    else:
        for i in range(0, len(word) // 2):
            if word[i] != word[len(word) - i - 1]:
                print("The string is not a palindrome.")
                return
        print("The string is a palindrome.")

# Test the function
while True:
    string = input("Enter a string (or type 'exit' to quit): ")
    if string.lower() == 'exit':
        print("Goodbye!")
        break
    checkstring(string)