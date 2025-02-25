class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0
        for end in range(len(s)):
            frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[end]])

            # move the start pointer towards right if the current
            # window is invalid
            is_valid = (end + 1 - start - max_frequency <= k)
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = end + 1 - start

        return longest_substring_length


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find longest substring with 2 characters where one element has <= k count

        Find longest substring that has a character with count len - count = k

        maintain a counter 
        find maximum window that satisfies condition

        len(window) - max(counter.values()) <= k
        """
        l = 0
        res = 0
        counter = {}

        for r, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1
            while r-l+1 - max(counter.values()) > k:
                counter[s[l]] -= 1
                if counter[s[l]] == 0:
                    del counter[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Need to find substring where the substring is valid
        substring is valid if n=len substring - occurence of most common element is <= k

        windows

        l, r

        add right element to dict
        length = r-l+1

        while lenght - max > k:
            remove left elemetn

        0123456
        AABABBA
        l
           r
        window = {A: 3, B: 1}
        res = 4
        k = 1
        """

        l = r = 0
        window = collections.defaultdict(int)
        res = 0

        for r in range(len(s)):
            window[s[r]] += 1

            while (r-l+1) - max(window.values()) > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            res = max(res, r-l+1)
        return res
        
