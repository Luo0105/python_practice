# a = int(input('Enter a number: '))
# if a % 15 == 0:
#     print('Foo Bar')
# elif a % 3 == 0:
#     print('Foo')
# elif a % 5 == 0:
#     print('Bar')
#
# def check(n):
#     if n % 15 == 0:
#         return 'Foo Bar'
#     if n % 3 == 0:
#         return 'Foo'
#     if n % 5 == 0:
#         return 'Bar'
#     return '?'
#
# print(check(int(input('Enter a number: '))))

a = int(input('Enter a number: '))
result = []
if a % 3 == 0:
    result += 'Foo'
if a % 5 == 0:
    result += 'Bar'
print(' ',join.result)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [5, 2, 9, 1, 7]
bubble_sort(numbers)
print(numbers)
