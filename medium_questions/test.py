class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
    
def mergeTwo(A, B):
    res = []
    a, b = 0, 0

    while a < len(A) and b < len(B):
        if a == len(A):
            curr = B[b]
            b+=1
        elif b == len(B):
            curr = A[a]
            a += 1
        elif A[a].start < B[b].start:
            curr = A[a]
            a += 1
        else:
            curr = B[b]
            b += 1
        if res and res[-1].end >= curr.start:
            res[-1].end = max(res[-1].end, curr.end)
        else:
            res.append(curr)
    return res

A = [Interval(1, 5), Interval(10, 14), Interval(16, 18)]
B = [Interval(2, 6), Interval(8, 10), Interval(11, 20)]

C = mergeTwo(A, B)

# print([[i.start, i.end] for i in C])

schedule = [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]]

cur = schedule
while len(cur) > 1:
    temp = []
    for i in range(0, len(cur), 2):
        # print("HERE")
        if i == len(cur)-1:
            temp.append(cur[i])
        else:
            temp.append(mergeTwo(cur[i], cur[i+1]))
    cur = temp

Test = mergeTwo(schedule[0], schedule[1])
print([[i.start, i.end] for i in Test])
