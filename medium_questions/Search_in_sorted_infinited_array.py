def binary_search(arr,l,r,x):
    while l <= r:
        m = (r+l)//2
        if arr[m] > x:
            r = m-1
        elif arr[m] < x:
            l = m+1
        else:
            return m
    return -1


def findPos(a, key):
    start, end = 0, 1
    while a[end] < key:
        newStart = end + 1
        end += (end - start + 1)*2
        start = newStart
    return binary_search(a, start, end, key)
 
# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = findPos(arr,10)
if ans == -1:
    print ("Element not found")
else:
    print("Element found at index",ans)