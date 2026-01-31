## LEET CODE APPROACH : Add Two Numbers 
TOPICS - [ Linked List, Math, Recursion ]

## Problem
Requires adding two non-negative integers represented as reversed linked lists and returning the sum as a new linked list. Each node holds a single digit, so you simulate addition digit-by-digit from the least significant digit while handling carries

## Intuition
The key insight is that numbers are stored in reverse order in linked lists (least significant digit first), so we can add them digit-by-digit from left to right, just like manual addition. We track a carry for overflow and use a dummy_head to simplify building the result list.

## Solution Strategy
Use a dummy node; iterate both lists + carry, append node with (sum % 10), carry = sum // 10; advance pointers until all exhausted.

## Approach
Initialize a dummy node and current pointer for the result list

While either input list has nodes or there's a carry:

- Extract digit values (0 if list exhausted)

- Compute sum with carry, get new digit and updated carry using divmod

- Create new node with sum digit, advance pointers

Return the next of dummy head (skips the dummy)

This simulates addition column-by-column with carry propagation.

## Complexity 

- Time Complexity: O(max(n,m)) where n and m are lengths of l1 and l2

- Space Complexity: O(max(n,m)) for the output linked list