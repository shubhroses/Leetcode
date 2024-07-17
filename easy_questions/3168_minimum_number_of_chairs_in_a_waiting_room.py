class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        cur = 0
        for c in s:
            if c == 'E':
                cur += 1
            elif c == 'L':
                cur -= 1
            res = max(res, cur)
        return res

        # 3168_minimum_number_of_chairs_in_a_waiting_room.py