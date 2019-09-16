class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        dict_count = collections.Counter(arr1) 
        for i in arr2:
            ans.extend([i]*dict_count.pop(i)) #adding numbers which are both in arr1 and arr2
        for i in range(1001):
            if i in dict_count:
                ans.extend([i]*dict_count[i])    #adding numbers which are only in arr1 and not in arr2    
        return ans

# O(1001) time and O(len(arr1)) space