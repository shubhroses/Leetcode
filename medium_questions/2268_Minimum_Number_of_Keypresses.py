class Solution:
    def minimumKeypresses(self, s: str) -> int:
        c = {}
        for char in s:
            c[char] = c.get(char, 0) + 1

        ans = cnt = 0
        for i, freq in enumerate(sorted(c.values(), reverse=True)):
            if i % 9 == 0:
                cnt += 1
            ans += cnt * freq
        return ans