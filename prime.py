# prime number
import math

def is_prime(num):
    if num < 2:
        return False
    for a in range (2, math.isqrt(num)+1):
        if num % a == 0:
            break
    else:
        return True


n = int(input("Enter a number: "))
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")