def narcissistic_number_or_not(number):
    if number <= 0:
        return False

    original_number = number
    length = len(str(number))
    sum = 0

    while number > 0:
        digit = number % 10
        sum += digit ** length
        number //= 10

    return sum == original_number

print(narcissistic_number_or_not(15))