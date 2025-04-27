# prime number
n = int(input("Enter a number: "))
for a in range (2, n):
    if n % a == 0:
        print(n, 'equals', a, '*', n//a)
        break
else:
    print(n, 'is a prime number')
