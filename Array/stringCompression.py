lass Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        else:
            i, j, length = -1, 1, 1
            while j <= len(chars):
                while j < len(chars) and chars[j] == chars[j-1]:
                    j += 1 
                    length += 1
                i += 1
                chars[i] = chars[j-1]
                if length != 1:
                    for number in str(length):
                        i += 1
                        chars[i] = number
                j += 1
                length = 1
            return i + 1
#O(N) time and O(1) space
