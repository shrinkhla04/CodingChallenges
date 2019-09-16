class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        dict_count = {} #store count of elements which are both in arr1 and arr2
        
        
        diff = [] #store elements which are not in arr2
        
        """"can also use collections.counter to create dict_count array and not use diff list but then would have to pop element from collections.counter if it is presnet both in arr1 and arr2"""
        for i in arr2:
            dict_count[i] = 0
        
        for i in arr1:
            if i in dict_count: #by saving arr2 elements as hash table ,their lookup time here is o(1), otherwise the lookup time for elements which are not in arr2 would be o(len(arr2))
                dict_count[i] += 1
            else:
                diff.append(i)
        
        for i in arr2:
            ans.extend([i]*dict_count[i])
        
            
            
        """since we don't have the counts for diff elements we would have to sort diff and then extend ans by diff. However, had we used collections.counter then we could pop elements which we have already added to ans and then add the rest of the elements in ascending order by iterating over a range of 1001 as arr1[i] can be in that range"""
        diff.sort()
        ans.extend(diff)
        return ans
        
#O(nlogn) time for worst case when there are arr2 is empty or when arr2 has very less elements
#O(len(arr1)) space