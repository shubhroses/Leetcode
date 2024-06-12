class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundA, foundB, foundC = False, False, False
        A, B, C = target
        for a, b, c in triplets:
            if a == A and b <= B and c <= C:
                foundA = True
            if b == B and a <= A and c <= C:
                foundB = True
            if c == C and a <= A and b <= B:
                foundC = True
        if foundA and foundB and foundC:
            return True
        return False

        
