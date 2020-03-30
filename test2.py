def find_unique_numbers(numbers):
    import collections
    arr = []
    count = collections.Counter(numbers)
    for key in count:
        if count[key] == 1:
            arr.append(key)
    return arr

print(find_unique_numbers([1, 2, 1, 3]))