# sort
def try_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(i+1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

numbers = [3, 5, 7, 12, 1, 20]
try_sort(numbers)
print(numbers)

#######################################

def min_index(array, minimum_index, current_index):
    if array[current_index] < array[minimum_index]:
        return current_index
    else:
        return minimum_index

def find_the_minimum(array, _from):
    minimum_index = _from
    for current_index in range(_from, len(array)):
        minimum_index = min_index(array, minimum_index, current_index)
    return minimum_index

def swap(array, current_index, minimum_index):
    array[current_index], array[minimum_index] = array[minimum_index], array[current_index]

def readable_sort(array):
    if len(array) < 2: return array
    for start_index in range(len(array)):
        minimum_index = find_the_minimum(array, _from=start_index)
        swap(array, start_index, minimum_index)
    return array


#array = []
#array = [1]
#array = [1, 2] #-> [1, 2]
#array = [2,1] # -> [1, 2]
#print(array)
assert readable_sort([]) == []
assert readable_sort([1]) == [1]
assert readable_sort([1, 2]) == [1, 2]
assert readable_sort([2, 1]) == [1, 2], readable_sort([2, 1])
assert readable_sort([1, 2, 3]) == [1, 2, 3]
assert readable_sort([2, 1, 3]) == [1, 2, 3]
assert readable_sort([2, 3, 1]) == [1, 2, 3], readable_sort([2, 3, 1])
#print(array)