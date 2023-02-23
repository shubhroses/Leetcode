def search_min_diff_element(arr, key):
    l, r = 0, len(arr)-1
    minDist = float("inf")
    curClosest = arr[0]
    while l <= r:
        m = (r+l)//2
        if arr[m] 

    return

def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))