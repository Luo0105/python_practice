def pyramid(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    for i in range(1,n+1):
        print(' '*(n-i+1),'* '*i)


a = int(input('Enter a number: '))
pyramid(a)

