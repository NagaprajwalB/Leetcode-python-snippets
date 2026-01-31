from typing import Optional 

class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Logic Part 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0) 
        curr = dummy_head
        carry = 0 
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, sum_val = divmod(val1 + val2 + carry, 10) 
            
            curr.next = ListNode(sum_val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 

        return dummy_head.next
    
# TESTING EXAMPLE 

sol = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = sol.addTwoNumbers(l1, l2)

print("Result head:", result.val if result else "None")
curr = result
vals = []
while curr:
    vals.append(str(curr.val))
    curr = curr.next
print("Full result:", " -> ".join(vals) + " -> None" if vals else "Empty")

# Logic: Traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous addition.
# Create new nodes for the resulting linked list to store the sum digit by digit. Continue until all digits and carry are processed.  
# Use a dummy head to simplify list construction and return the next node after processing.          
# Handle cases where the lists are of different lengths and when there's a carry left after the last addition.

# Time Complexity: O(max(m, n)) where m and n are the lengths of the two linked lists.
# Space Complexity: O(max(m, n)) for the new linked list created to store the result.

# This approach ensures we correctly add two numbers represented as linked lists in reverse order.
# Each node contains a single digit, and we return the sum as a linked list in the same format.
