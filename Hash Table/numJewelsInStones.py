class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #store J in either hash table or set for O(1) search
        if not S:
            return 0
        Jewel_hash = {}
        for jewel in J:
            Jewel_hash[jewel] = jewel
        number_jewels = 0
        for stone in S:
            if stone in Jewel_hash:
                number_jewels += 1
        return number_jewels
"""O(J) space for storing J in hash . We can consider 
this as constant space because there will be 26*2 caracters at most so it is constant space """

"""O(J+S) time for storing J in hash and iterating over S , however storing 
J elements in hash will be constant time as a maximum of 26*2 characters .
So, time complexity will be just O(S) time"""