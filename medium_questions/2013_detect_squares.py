class DetectSquares:
    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

"""
(x, y)
get all points on x axis 
get all points on y axis

(v, w)
find pairs that match distance
abs(v - x) = abs(w - y)

For matching pairs look for 3rd match 

xAxis = {x: [vals]}
yAxis = {y: [vals]}

xAxis = {
    3: [2, 10],
    11:[2]
}
yAxis = {
    10: [3]
    2: [3, 11]
}
[11, 10]

11: 2
10: 3
"""
