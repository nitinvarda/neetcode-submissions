class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums
        
        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
            
        hp = []
        
        for n in count:
            heapq.heappush(hp, (count[n], n))
            
            if len(hp) > k:
                heapq.heappop(hp)
                
        
        return [n for freq, n in hp]
        