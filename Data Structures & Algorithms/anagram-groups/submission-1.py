class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        
        ans_map = {}
    
        count = [0] * 26
    
        for sr in strs:
            count = [0] * 26
            # print(sr)
            for v in sr:
                count[ord(v) - ord('a')] += 1
            
            string_count = tuple(count)
            
            # print(string_count)
            if string_count in ans_map:
                ans_map[string_count] += [sr]
            else:
                ans_map[string_count] = [sr]
        
        return list(ans_map.values())
        