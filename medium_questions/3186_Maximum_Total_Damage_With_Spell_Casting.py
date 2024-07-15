class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # 3186_Maximum_Total_Damage_With_Spell_Casting.py
        power.sort(reverse=True)
        
        memo = {}
        def helper(i, prev):
            if i == len(power):
                return 0
            
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            take_current = 0
            if abs(power[i] - prev) > 2 or prev == power[i]:
                take_current = power[i] + helper(i + 1, power[i])
                
            leave_current = helper(i + 1, prev)
            
            memo[(i, prev)] = max(take_current, leave_current)
            return memo[(i, prev)]
        
        return helper(0, -2)
