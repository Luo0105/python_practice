def selection_sort(numbers):
    for i in range(len(numbers)-1):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

list1 = [64, 25, 12, 22, 11]
selection_sort(list1)
print(list1)