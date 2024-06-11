class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        elements = collections.Counter(hand)
        print(elements)

        for _ in range(len(hand) // groupSize):
            minimum = min(elements)
            for _ in range(groupSize):
                if minimum not in elements:
                    return False
                elements[minimum] -= 1
                if elements[minimum] == 0:
                    del elements[minimum]
                minimum += 1
        return True


        
