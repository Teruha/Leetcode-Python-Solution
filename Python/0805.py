class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B > A: A, B = B, A
        if B == 1: return A
        if B == 0: return 0

        res = 0
        for i in range(B):
            if B & 1:
                res += A << i
            B >>= 1

        return res