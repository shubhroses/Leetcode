class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        """
        damage = [2, 7, 4, 3]
        armor = 4
                    r1    r2   r3   r4
        health = 13 -> 11 -> 4 -> 4 -> 1
        
        health = 17
        
        When do we use the armor
        Could use armor at any index <= armor level
        
        Take sum + 1, find max element less than or equal to armour 
        
        sort and iterate through until reach element <= armour
        
        
        
        """
        totPlus1 = sum(damage) + 1
        totPlus1 -= min(armor, max(damage))
        return totPlus1

        totPlus1 = sum(damage) + 1
        totPlus1 -= min(armor, max(damage))
        return totPlus1