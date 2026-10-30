class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            if num in values:
                return [values.get(num), i]
            values.update({target-num: i})

