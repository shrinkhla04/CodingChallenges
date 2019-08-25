#!/usr/bin/env python3

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack_nums2=[] 
        """ All elements of nums2 for which the next greater element is still to be searched are stored in the stack"""
        dic_nums2={}

        """ All the next greater elements for elements in nums2 are stored in a dictionary. If an element in nums2 does not have a next greater element then it is never added to the dictionary """
        for i in nums2:
            while stack_nums2 != [] and i > stack_nums2[-1]:
                dic_nums2[stack_nums2.pop()] = i 
                """As soon as the next greater element to the last element of the nums2 stack is found then it's corresponding next greater element is stored as it's value in the dictionary. 
                Since the next greater element to this element has been found so this element is thus removed from the stack. 
                All those elements which do not have a greater element to them to their right in  nums2 are never added to the dictionary """
            stack_nums2.append(i)

        """As this algorithm requires a check on the last element of the list and it's removal if the check is true so a stack is the most suitable data structure to store the elements for which the next greater element is to be found"""
    
    """ A stack is used to store all the elements for which next greater element is still to be found because 'i' has to be checked as a potential greater element for each of it's elements to it's left
        In case it is found as a potential greater element for an element to it's left then that element can be popped from the stack but 'i' is still to be checked as a potential
        greater element for the second last element in the stack. In case it turns out to be the next greater element for the second last element as well , then it has to be checked as a potential 
        greater element for the third last element in the stack and so on until 'i' fails to be a potential greater element for an element in the stack. 
        
        As at a particular moment 'i' is checked as a potential gretaer element for the last element in the stack and in case it does turn out to be then the last element of the stack can be removed (because it's next greater element has already been found) so a stack is the most suitable data structure for storing the elements whose next greater element."""
        
        next_greater_element=[]
        print(dic_nums2)
        for j in nums1:
            if j in dic_nums2.keys():
                next_greater_element.append(dic_nums2[j])
            else:
                next_greater_element.append(-1)

        return(next_greater_element)

        
nextGreaterElement_object=Solution()
print(nextGreaterElement_object.nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1]))



