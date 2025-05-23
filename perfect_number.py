def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number(n):
    if n < 2:
        return False
    divisors = proper_divisors(n)
    return sum(divisors) == n

numbers = [6, 28, 12, 496, 8128, 33550336]
for number in numbers:
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is NOT a perfect number.")
