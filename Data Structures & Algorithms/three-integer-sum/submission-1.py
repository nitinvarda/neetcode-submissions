class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        
        for i in range(len(arr)):
            if i==0 or arr[i] != arr[i-1]:
                self.twoSum2(arr, i, result)
        
        return result

    def twoSum2(self, arr, i, result):
        left = i+1
        right = len(arr) - 1
        
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < 0 :
                left += 1
            elif sum > 0 :
                right -= 1
            else:
                result.append([arr[i],arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1