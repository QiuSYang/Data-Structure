# 树结构算法题

## 1. 二叉树题目的一个难点就是，如何把题目的要求细化成每个节点需要做的事情。

### LeetCode-226: 翻转二叉树

翻转一棵二叉树。

示例：

    输入：
    
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    输出：
    
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

linked：https://leetcode-cn.com/problems/invert-binary-tree

codes: 
    
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def invertTree(self, root: TreeNode) -> TreeNode:
            """前序遍历树"""
            if root is None:
                return None 
            temp = root.left 
            root.left = root.right 
            root.right = temp  # 左右子树交换
    
            # 让左右子节点继续翻转它们的子节点
            self.invertTree(root.left)
            self.invertTree(root.right)
    
            return root 

## LeetCode-116. 填充每个节点的下一个右侧节点指针

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：

    你只能使用常量级额外空间。
    使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

示例：

![116_sample](images/116_sample.png)

    输入：root = [1,2,3,4,5,6,7]
    输出：[1,#,2,3,#,4,5,6,7,#]
    解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node

题目的意思就是把二叉树的每一层节点都用 next 指针连接起来：

![image](images/116_sample.png)

而且题目说了，输入是一棵「完美二叉树」，形象地说整棵二叉树是一个正三角形，除了最右侧的节点 next 指针会指向 null，其他节点的右侧一定有相邻的节点。

这道题怎么做呢？把每一层的节点穿起来，是不是只要把每个节点的左右子节点都穿起来就行了？

我们可以模仿上一道题，写出如下代码：

    Node connect(Node root) {
        if (root == null || root.left == null) {
            return root;
        }
    
        root.left.next = root.right;
    
        connect(root.left);
        connect(root.right);
    
        return root;
    }

这样其实有很大问题，再看看这张图：

![image](images/116_sample.png)

节点 5 和节点 6 不属于同一个父节点，那么按照这段代码的逻辑，它俩就没办法被穿起来，这是不符合题意的。

回想刚才说的，**二叉树的问题难点在于，如何把题目的要求细化成每个节点需要做的事情**，但是如果只依赖一个节点的话，肯定是没办法连接「跨父节点」的两个相邻节点的。

那么，我们的做法就是增加函数参数，一个节点做不到，我们就给他安排两个节点，「将每一层二叉树节点连接起来」可以细化成「将每两个相邻节点都连接起来」：

    // 主函数
    Node connect(Node root) {
        if (root == null) return null;
        connectTwoNode(root.left, root.right);
        return root;
    }
    
    // 辅助函数
    void connectTwoNode(Node node1, Node node2) {
        if (node1 == null || node2 == null) {
            return;
        }
        /**** 前序遍历位置 ****/
        // 将传入的两个节点连接
        node1.next = node2;
    
        // 连接相同父节点的两个子节点
        connectTwoNode(node1.left, node1.right);
        connectTwoNode(node2.left, node2.right);
        // 连接跨越父节点的两个子节点
        connectTwoNode(node1.right, node2.left);
    }
    
这样，connectTwoNode 函数不断递归，可以无死角覆盖整棵二叉树，将所有相邻节点都连接起来，也就避免了我们之前出现的问题，这道题就解决了。

    """
    # Definition for a Node.
    class Node:
        def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
            self.val = val
            self.left = left
            self.right = right
            self.next = next
    """
    
    class Solution:
        def connect(self, root: 'Node') -> 'Node':
            if root is None:
                return root 
            self.tow_node_connect(root.left, root.right)
            return root 
    
        def tow_node_connect(self, node1: 'Node', node2: 'Node') -> 'Node':
            if node1 is None or node2 is None:
                return 
    
            # 前序遍历
            node1.next = node2
    
            self.tow_node_connect(node1.left, node1.right)  # 左右节点连接
            self.tow_node_connect(node2.left, node2.right)
    
            self.tow_node_connect(node1.right, node2.left)  # 右节点与左节点相连

## LeetCode-114. 二叉树展开为链表

给你二叉树的根结点 root ，请你将它展开为一个单链表：

    1. 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
    2. 展开后的单链表应该与二叉树 先序遍历 顺序相同。
 

示例 1：

![image](images/flaten.jpg)

    输入：root = [1,2,5,3,4,null,6]
    输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：

    输入：root = []
    输出：[]
    
示例 3：

    输入：root = [0]
    输出：[0]

linked：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list

代码实现：
    
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def flatten(self, root: TreeNode) -> None:
            """
            Do not return anything, modify root in-place instead.
            """
            if root is None:
                return root 
            # 后序遍历
            self.flatten(root.left)
            self.flatten(root.right)
            
            # 1、左右子树已经被拉平成一条链表
            left = root.left
            right = root.right 
    
            # 2、将左子树作为右子树
            root.left = None  # 左节点置空
            root.right = left  # 右节点连接当前节点的左节点
    
            # 3、将原先的右子树接到当前右子树的末端
            temp = root 
            while temp.right is not None:
                temp = temp.right  # 找到右节点为空的位置
            temp.right = right  # 左右节点连接
    
            return root

## 把题目的要求细化，搞清楚根节点应该做什么，然后剩下的事情抛给前/中/后序的遍历框架就行了，我们千万不要跳进递归的细节里，你的脑袋才能压几个栈呀。

## LeetCode-124. 二叉树中的最大路径和

路径被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：

![image](images/2.jpg)

    输入：root = [1,2,3]
    输出：6
    解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2:

![image](images/3.jpg)

    输入：root = [-10,9,20,null,null,15,7]
    输出：42
    解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

Linked：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum

**代码实现：递归，中序遍历，深度优先搜索**, 节点的最大贡献：**以该节点出发最大路径和**

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        max_path_sum = float("-inf")
        def maxPathSum(self, root: TreeNode) -> int:
            root_gain = self.maxGain(root)
    
            return self.max_path_sum
    
        def maxGain(self, root: TreeNode) -> int:
            """递归计算每个节点的最大贡献 --- 后序遍历 --- dfs"""
            if root is None:
                # 节点为空, 那么贡献度为空
                return 0 
    
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            left_gain = max(self.maxGain(root.left), 0)  # 当前节点左树的最大贡献
            right_gain = max(self.maxGain(root.right), 0)  # 当前节点右树的最大贡献
    
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            current_node_gain = root.val + left_gain + right_gain
    
            # 更新最大路径
            self.max_path_sum = max(self.max_path_sum, current_node_gain)
    
            return root.val + max(left_gain, right_gain)  # 当前节点的最大贡献度

## LeetCode-654. 最大二叉树

给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

二叉树的根是数组 nums 中的最大元素。

    1. 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
    2. 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
    3. 返回有给定数组 nums 构建的 最大二叉树 。
    
示例 1：

![image](images/4.jpg)

    输入：nums = [3,2,1,6,0,5]
    输出：[6,3,5,null,2,0,null,null,1]
    解释：递归调用如下所示：
    - [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
        - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
            - 空数组，无子节点。
            - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
                - 空数组，无子节点。
                - 只有一个元素，所以子节点是一个值为 1 的节点。
        - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
            - 只有一个元素，所以子节点是一个值为 0 的节点。
            - 空数组，无子节点。

Linked：https://leetcode-cn.com/problems/maximum-binary-tree

代码实现：

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
            """前序遍历, 先构造跟节点"""
            if not nums: 
                return None
            # 数组最大值划分左右子树
            max_value, max_index = float("-inf"), 0 
            for idx, element in enumerate(nums):
                if element > max_value:
                    max_value = element
                    max_index = idx 
            
            left_nums = nums[:max_index] 
            right_nums = nums[max_index+1:]
    
            root = TreeNode(max_value)  # 构建当前根节点
            root.left = self.constructMaximumBinaryTree(left_nums)  # 构建左树
            root.right = self.constructMaximumBinaryTree(right_nums)  # 构建右树
    
            return root 

## LeetCode-105. 从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

**注意**:你可以假设树中没有重复的元素。

例如，给出

    前序遍历 preorder = [3,9,20,15,7]
    中序遍历 inorder = [9,3,15,20,7]

返回如下的二叉树：

      3
     / \
    9  20
      /  \
     15   7

Linked：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

代码实现：

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            """根据前序, 中序重新构建树"""
            return self.build(preorder, 0, len(preorder) - 1, 
                              inorder, 0, len(inorder) - 1)
    
        def build(self, preorder: List[int], pre_start: int, pre_end: int, 
                  inorder: List[int], in_start: int, in_end: int):
            """递归构建树, 前序遍历
                pre_start: 前序起点, pre_end：前序终点, 
                in_start: 中序起点, in_end: 中序终点"""
            if pre_start > pre_end:
                # base case, 树元素访问完毕
                return None 
            
            root_value = preorder[pre_start]  # 前序遍历第一个值为根节点值
            # 确定根节点在中序遍历的位置, 中序遍历根节点将树分为左子树与右子树
            inorder_root_index = 0 
            for idx, value in enumerate(inorder):
                if root_value == value:
                    inorder_root_index = idx
                    break 
    
            root = TreeNode(root_value)  
            # 中序遍历的作用就是协助分离左右子树, 前序的作用就是确定根节点
            left_size = inorder_root_index - in_start  # 左子树的大小
            root.left = self.build(preorder, pre_start + 1, pre_start + left_size, 
                                   inorder, in_start, inorder_root_index - 1)
            root.right = self.build(preorder, pre_start + left_size + 1, pre_end, 
                                    inorder, inorder_root_index + 1, in_end)
            
            return root 
            
## LeetCode-106. 从中序与后序遍历序列构造二叉树

根据一棵树的中序遍历与后序遍历构造二叉树。

**注意**:你可以假设树中没有重复的元素。

例如，给出

    中序遍历 inorder = [9,3,15,20,7]
    后序遍历 postorder = [9,15,7,20,3]
    
返回如下的二叉树：

      3
     / \
    9  20
      /  \
     15   7

Linked：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal

代码实现：

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
            return self.build(inorder, 0, len(inorder) - 1, 
                              postorder, 0, len(postorder) - 1)
    
        def build(self, inorder: List[int], in_start: int, in_end: int, 
                  postorder: List[int], post_start: int, post_end: int) -> TreeNode:
            """中序遍历拆解左右子树, 后序遍历寻根"""
            if post_start > post_end:
                # base case, 节点子树为空
                return None 
    
            root_value = postorder[post_end]
            root_index = 0
            for idx, value in enumerate(inorder):
                if value == root_value:
                    root_index = idx
                    break 
            
            root = TreeNode(root_value)
            left_size = root_index - in_start  # 左子树的节点数
            # 递归调用建子树
            root.left = self.build(inorder, in_start, root_index - 1, 
                                   postorder, post_start, post_start + left_size - 1)
            root.right = self.build(inorder, root_index + 1, in_end, 
                                    postorder, post_start + left_size, post_end - 1)
    
            return root 

## LeetCode-652. 寻找重复的子树

Linked: https://leetcode-cn.com/problems/find-duplicate-subtrees/submissions/

代码实现:

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
            result = []
            sub_tree = {}  # 哈希存储子树是否出现过
            def traverse(root: TreeNode) -> str:
                """后续遍历"""
                if root is None:
                    return "#"
                
                # 树序列化
                left_str = traverse(root.left)
                right_str = traverse(root.right)
                sub_tree_str = left_str + "->" + right_str + "->" + str(root.val)  
                # print(sub_tree_str)
                # 序列化子树作为可以
                if sub_tree_str not in sub_tree:
                    sub_tree[sub_tree_str] = 0 
                else:
                    sub_tree[sub_tree_str] += 1 
                
                if sub_tree[sub_tree_str] == 1:
                    # 重复子树加入结果列表
                    result.append(root)
                
                return sub_tree_str
            
            traverse(root)
    
            return result
    