class Solution:
    def rotatedDigits(self, N: int) -> int:
        counter = 0
        for i in range(1,N+1):
            i = str(i)
            counter+= (any(d in '2569' for d in i) and all(d not in '347' for d in i))
        """if none of the digits are in 2569 then it can't be a good number  as in that case either the number consists of all digits from '347' or from '108'or from a mixture of '108347'. In all three cases the number can't be a good number """
        return counter
                    
    #Time : O(NlogN) as for each number we check each digit and number of digits in a number are logN
    #Space : O(log N) as at a time we are storing digits of a single number and number of digits in a single number are logN