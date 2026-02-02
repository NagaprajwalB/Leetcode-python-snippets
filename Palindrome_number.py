# LOGIC PART FOR PALINDROME NUMBER PROBLEM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        
        reversed_num = 0
        temp = x 

        while temp > 0:
            reversed_num = reversed_num * 10 + temp %  10
            temp //= 10
        
        return x == reversed_num

# TEST PART
if __name__ == "__main__":
     sol = Solution()
     print(sol.isPalindrome(121))
     print(sol.isPalindrome(-121))
     print(sol.isPalindrome(10))