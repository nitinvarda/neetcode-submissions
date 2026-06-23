class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
    
        occurance = [0] * 26
        ans = 0
        max_occurance = 0

        for right in range(len(s)):
            occurance[ord(s[right])-ord('A')] += 1
            max_occurance = max(max_occurance,occurance[ord(s[right])-ord('A')])
            if right - left + 1 - max_occurance > k:
                occurance[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans,right-left+1)
                
        
        return ans