def count_frequency(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Test case
arr1 = [10, 5, 15, 10, 5, 10]
frequency = count_frequency(arr1)

for key, value in frequency.items():
    print(f"Element {key} occurs : {value} times", count_frequency(arr1))

arr2 = [2, 2, 3, 4, 4, 2]
frequency = count_frequency(arr2)

for key, value in frequency.items():
    print(f"Element {key} occurs : {value} times", count_frequency(arr2))