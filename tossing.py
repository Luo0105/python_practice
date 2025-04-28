import random

results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(10):
    result1 = random.randint(1, 6)
    print(f'Roll {i+1}: {result1}')
    results[result1] += 1

print()
print("Results:")
for point, count in results.items():
    print(f'{point}: {count} times')

