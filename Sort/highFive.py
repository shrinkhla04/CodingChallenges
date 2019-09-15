
https://leetcode.com/problems/high-five/
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict_id = {}
        for i in items:
            if i[0] not in dict_id:
                dict_id[i[0]] = [i[1]]
            else:
                dict_id[i[0]].append(i[1])
        res = []
        for key in dict_id:
            dict_id[key].sort()
            avg_top_5 = sum(dict_id[key][-5:]) // 5
            res.append([key,avg_top_5])
        return res
            
#O(nlogn) : O(nlogn) time  for sorting and O(n) time for reading the items to the hash table
# O(n) space for hash table and res