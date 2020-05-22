class Solution:
    def permutation(self, S: str) -> List[str]:
        res=[]
        S=list(S)
        n=len(S)
        def helper(S,n,s=''):
            if len(s)==n:
                res.append(s)
            for i in range(len(S)):
                helper(S[:i]+S[i+1:],n,s+S[i])
        helper(S,n)
        return res