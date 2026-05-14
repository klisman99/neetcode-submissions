class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for key, value in enumerate(nums):
            diff = target - value
            if diff in values:
                return [values[diff], key]
            values[value] = key

        return []        