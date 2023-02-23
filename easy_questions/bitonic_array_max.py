def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start + end)//2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]

if __name__ == "__main__":
    print(find_max_in_bitonic_array([1, 3, 8, 14, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))
