# LEET CODE APPROACH : Palindrome number 

## Problem
Given an integer x, return true if x is a palindrome, and false otherwise.

## Intuition
To check if an integer is a palindrome, reverse its digits and compare with the original—e.g., 121 reversed is 121 (palindrome), but 123 reversed is 321 (not). Handle negatives as non-palindromes since they start with '-'.

## Approach
Convert the number to digits using modulo (%) and integer division (//), building the reverse iteratively in a loop until the number is 0, then check equality. This avoids string conversion for O(1) extra space.

## Time Complexity
O(d), where d is the number of digits (worst ~log10(x) + 1, or O(log n) effectively).

## Space Complexity
O(1), as we only use a few variables regardless of input size.