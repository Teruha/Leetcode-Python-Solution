class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1

        if n == 3:
            return 2

        sum = 1

        while n > 4:
            sum = sum * 3
            n = n - 3

        return n * sum