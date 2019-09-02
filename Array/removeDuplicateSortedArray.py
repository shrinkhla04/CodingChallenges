#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

""" 1.Two pointers are used such that one(i) is a slow runner and the other(j) is a fast runner
2. as long as nums[j] == nums[i], j is incremented to skip the duplicate.
3.As soon as nums[j] != nums[i] is encountered , the duplicate run has ended and this value at nums[j] must be copied to nums[i+1]
4. 'i' is then incremented 
5. steps 2, 3, 4 are repated until j reaches the end of the array
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums [j]:
                nums[i+1] = nums[j] 
                "anything between i and j is a duplicate of a value before i and thus has to be replaced with a non-duplicate after j"
                i = i+1
        return i+1 
    "when j will reach the end of the array no non duplicate value is left tp be iterated and all values until 'i' will be unique so i+1 is returned as that will be the length"
                

"""O(n) time as each of i and j traverse at most n steps 
eg if n=9 and i=0 and next non duplicate is at j = 6 , j has traversed 5 steps until now and then i will be incremented so i+j =6,
next when i = 1 and next non duplicate is at j =8, j has traversed 2 steps  and then i will be incremented so a total of 3 steps by both i and j and a total of 9 steps
"""

#O(1) space as in place
