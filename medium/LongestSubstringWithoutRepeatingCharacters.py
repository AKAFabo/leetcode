class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        current = ""
        best = 0

        for ch in s:

            if ch in current:
                idx = current.index(ch)
                current = current[idx + 1:]

            current += ch
            best = max(len(current), best)    

        return(best)    