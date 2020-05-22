class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        flag, ans = False, None
        def f(r):
            nonlocal flag, ans
            if r and not ans:
                f(r.left)
                if r is p:
                    flag = True
                elif flag:
                    ans, flag = r, False
                f(r.right)
        f(root)
        return ans