## LEET CODE APPROACH : Longest Substring Without Repetation 
TOPIC : [ Sliding windows, Hash Table, String ]

## Problem
Given a string s, find the length of the longest substring without duplicate characters.

## Intuition
The code solves the "Longest Substring Without Repeating Characters" problem using a sliding window to track the maximum length of a substring with unique characters.

## Approach
It uses a dictionary char_dict to store the most recent index of each character. A start pointer marks the window's left boundary and an end pointer (loop variable) expands the right. When a repeat is found, start jumps to just after the previous occurrence using max(start, char_dict[s[end]] + 1). The window length end - start + 1 updates max_len each step, ensuring O(n) efficiency by only moving pointers forward

## Complexity
- Time complexity:
O(n), where n is the string length, as each character is visited once and pointers advance linearly

- Space complexity:
O(min(n, |Σ|)), where |Σ| ≤ 128 for typical character sets like ASCII; the dictionary holds at most one entry per unique character.
