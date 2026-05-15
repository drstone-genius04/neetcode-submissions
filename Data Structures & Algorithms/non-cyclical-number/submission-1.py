class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        # Start fast one step ahead
        fast = self.sumOfSquare(n)
        
        # Move until they meet
        while slow != fast:
            fast = self.sumOfSquare(fast)
            fast = self.sumOfSquare(fast)
            slow = self.sumOfSquare(slow)
            
        # If they meet at 1, it's a happy number
        return fast == 1

    def sumOfSquare(self, n: int) -> int:
        output = 0
        while n > 0:
            digit = n % 10
            output += digit ** 2
            n //= 10
        return output