def first_duplicate(arr):
    start = set()
    for i in range(len(arr)):
        if arr[i] in start:
            return arr[i]
        else:
            start.add(arr[i])


res = first_duplicate([1, 2, 3, 2, 1])
print(res)
