from typing import List # import List for type hinting

# LOGIC PART 
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

if __name__ == "__main__": # Example usage
    s = Solution()
    result = s.twoSum([2, 7, 11, 15], 9)
    print(result)

# LOGIC: Use a dictionary to store the indices of the numbers we have seen so far.
# For each number, calculate its complement (target - number) and check if it exists in
# the dictionary. If it does, return the indices. If not, add the number and its index
# to the dictionary.