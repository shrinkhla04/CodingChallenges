#Soultion I

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        string_representation = [None]*n
        # start by checking if the number is multiple of both because if we'll start by checking if number is multiple of either one then if there is a number which is a multiple of both then it will first fall into the if condition which is checking if the number is  multiple of either one and will never fall into the if condition where it checks if number is multiple of both. So, in order to avoid this we'll start by checing if the number is multiple of both and if this is the case then it should produce the desired output and will thus never fall into the if conditions where it checks for multiples of either one

        for i in range(1,n+1):
            if i % 15 == 0:
                string_representation[i -1] = "FizzBuzz"
            elif i % 5 == 0:
                string_representation[i -1] = "Buzz"
            elif i % 3 == 0:
                string_representation[i -1] = "Fizz"
            else:
                string_representation[i -1] = str(i)
        return string_representation





                
#O(n) time and O(1) space as space required for returning the answer was anyway going to be used so space of the list string_representation does not count


#Soultion 2

"""if there are too many conditions to be checked for eg if we add Jazz as a mapping if the number is divisinble by 7 then by Soultion 1 , we would have to check
for the following 7 conditions:  1) divisible by 3,5,7 2) divisible by 3,5 3) divisible 3,7 4) divisible by 5,7 5) divisible by 3 6) divisble by 5 7) divisble by 7
Similarly if we add more mapping then conditions would keep increasing, so it is better to use string concatenation and check for just 3 conditions i.e. divisible by 3, 5, 7 . The number of coditions to be checked for will be equal to the number of mappings

"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        string_representation = [""]*n

        for i in range(1,n+1):
            if i % 3 == 0:
                string_representation[i - 1] += "Fizz"
            if i % 5 == 0:
                string_representation[i - 1] += "Buzz"
            if string_representation[i - 1] == "":
                string_representation[i - 1] = str(i)
        return string_representation

#Soultion 3 

""" In solution 2 if there are too many mapping then thenumber of conditions to be checked to will also increase to too many and might make the code look ugly so it is better if we hash the mappings such that for every number that we iterate over form  1 to N then , we would check if it is divisible by any of the keys , if yes then we will concatenate the hash value of that key to the string representation for that number.
Please note that when we iterate over the keys . the keys should be sorted which might not be possible in a hash
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        string_representation = [""]*n
        hash_table = { 3:'Fizz', 5:'Buzz'}
        for i in range(1,n+1):
            for j in hash_table.keys():
                if i % j == 0:
                    string_representation[i-1] += hash_table[j]
            if string_representation[i - 1] == "":
                string_representation[i - 1] = str(i)                      
        return string_representation
                
#O(n) time as for every n we are checking iterating over constant number of keys equal to the number of mapping so that is cosidered constant and O(1) space

