import math

def is_prime(num):
    if not isinstance(num, (int, float)) or not float(num).is_integer():
        return False  # 非整数
    num = int(num)
    if num < 2:
        return False
    for a in range(2, math.isqrt(num) + 1):
        if num % a == 0:
            return False
    return True

def get_valid_number():
    while True:
        try:
            raw = input("Enter a number: ")
            num = float(raw)
            if not num.is_integer():
                print("Please enter a whole number.")
                continue
            return int(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    n = get_valid_number()
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

main()
