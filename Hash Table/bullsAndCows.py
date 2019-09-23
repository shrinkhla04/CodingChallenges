class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hash_table = {}
        bulls = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in hash_table:
                    hash_table[secret[i]] = 1  
                else:
                    hash_table[secret[i]] += 1
        cows = 0
        for i in range(len(guess)):
            if guess[i] != secret[i] and guess[i] in hash_table and hash_table[guess[i]] > 0:
                hash_table[guess[i]] -= 1
                cows += 1
        return str(bulls) + "A" + str(cows) + "B"

#O(n) time and O(1) space