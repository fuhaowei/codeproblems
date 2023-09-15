class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        low = 0
        high = 0
        lens = len(s)
        length = 0
        highest = 0

        freq_dict = defaultdict(int)

        while high < lens:

            freq_dict[s[high]] += 1
            length += 1
       

            while max(freq_dict.values()) > 1:
                freq_dict[s[low]] -= 1
                low += 1
                length -= 1

            highest = max(length, highest)

            high += 1

        return highest

            

        