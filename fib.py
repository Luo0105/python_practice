def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

a = int(input('Enter a number: '))
print('The ', a ,'th Fibonacci number is ', fib(a))
