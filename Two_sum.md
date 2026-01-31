
# LEET CODE APPROACH : How the Two Sum Algorithm Works 

## Problem
Given an array of numbers and a target value, find two numbers that add up to the target and return their indices.

## Intuition:

Use a hash map to remember numbers we have already seen so we can check in constant time whether the current number’s complement (target − current) has appeared before.

## Solution Strategy
The code uses a hash map (dictionary) to solve this efficiently in one pass through the array.

## Approach:

Iterate once over the array while maintaining a dictionary that maps each number to its index.

For each element num at index i, compute complement = target - num.

If complement is already in the dictionary, return [num_dict[complement], i] because we have found the two indices that add up to the target.

Otherwise, store the current number and its index in the dictionary with num_dict[num] = i and continue scanning the array.

Since the problem guarantees exactly one solution and disallows using the same element twice, we can safely return as soon as we find such a pair.

## Example
If `nums = [2, 7, 11, 15]` and `target = 9`:

- At index 0: `num=2`, `complement=7`, dictionary is empty, so store `{2: 0}`
- At index 1: `num=7`, `complement=2`, found 2 in dictionary at index 0, return `[0, 1]`

## Complexity:

### Time complexity: 
- O(n), because we perform one pass over the array and each dictionary lookup and insertion is O(1) on average.

### Space complexity: 

- O(n), since in the worst case we may store all n elements of the array in the dictionary.

## Why It's Efficient
The algorithm is clever because it avoids checking every possible pair of numbers (which would be O(n²)), instead using the dictionary for instant lookups.