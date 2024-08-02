class Solution:
  def minimum(self, apples: List[int], capacity: List[int]) -> int):
    n = sum(apples)
    capacity.sort(reverse=True)

    for i, c in enumerate(capacity):
      if allApples <= c:
          return i+1
      allApples -= c
