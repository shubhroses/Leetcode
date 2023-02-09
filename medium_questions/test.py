def can_attend_all_appointements(intervals):
    intervals.sort(key = lambda x:x[0])

    for i in range(1, len(intervals)):
        prevS, prevE = intervals[i-1]
        curS, curE = intervals[i]
        if curS < prevE:
            return False
    return True

print(can_attend_all_appointements([[1,4], [2,5], [7,9]]))
print(can_attend_all_appointements([[6,7], [2,4], [8,12]]))
print(can_attend_all_appointements([[4,5], [2,3], [3,6]]))