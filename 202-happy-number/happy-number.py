class Solution(object):
    def isHappy(self, n):
        def fun(num):
            sum = 0
            while num > 0:
                d = num % 10
                sum += d * d
                num //= 10
            return sum

        slow = n
        fast = n

        while True:
            slow = fun(slow)
            fast = fun(fun(fast))

            if slow == fast: 
                break

        return slow == 1                         