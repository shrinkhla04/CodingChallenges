#https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        #creating hash table for elements in order with values as their indices in order
        for i in range(len(order)):
            order_dict[order[i]] = i
        characters_equal = False
        for i in range(len(words) - 1):
            for k in range(min(len(words[i]),len(words[i+1]))):
                if order_dict[words[i][k]] < order_dict[words[i+1][k]]:
                    characters_equal = False
                    break
                elif order_dict[words[i][k]] > order_dict[words[i+1][k]]:
                    characters_equal = False
                    return False
                else:
                    characters_equal = True
            
            #character_equal will be true only if all charcters are equal 
            if characters_equal:
                if len(words[i]) > len(words[i+1]):
                    return False
                
            
            
        
        return True

#O(order) extra space which can be 0(1) as well as len(order) is always 26 characters
#O(C) where C is the content of words as in worst case when all words are equal the algorithm would compare every character of every work with every character of the nexr word in the list
        
        
            