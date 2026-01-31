from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

if __name__ == "__main__":
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result)