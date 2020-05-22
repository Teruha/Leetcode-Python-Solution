# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        result = []
        depth = 0
        def count_depth_num(Node,depth):
            if not Node:
                return
            if Node:
                depth += 1
            if len(res) < depth:
                res.append([])
            res[depth-1].append(Node.val)
            count_depth_num(Node.left,depth)
            count_depth_num(Node.right,depth)
        count_depth_num(tree,depth) # 按照深度将节点值val添加到相应的和深度数组res，执行后res=[[1], [2, 3], [4, 5, 7], [8]]

        # 接着按照分好的深度节点val数组生成相应的深度链表
        for i in res:
            head = ListNode(None)
            pre = head
            for node_val in i:
                new_node = ListNode(node_val)
                pre.next = new_node
                pre = new_node
            result.append(head.next)
        return result