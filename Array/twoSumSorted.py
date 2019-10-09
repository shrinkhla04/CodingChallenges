class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) -1
        sum_curr = numbers[start] + numbers[end]
        while sum_curr != target:
            if sum_curr < target:
                start += 1
            else:
                end -= 1
            sum_curr = numbers[start] + numbers[end]
        return [start + 1, end + 1]
#O(N) time and O(1) space