class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
    
        if len(s) == 1:
            return 1
            
        
        longest = 0
        map = set()
        left = 0
        right = 0
        
        while right < len(s):
            c = s[right]
            while c in map:
                map.discard(s[left])
                left += 1
            map.add(c)
            longest = max(longest,right-left+1)
            right += 1
        return longest
        