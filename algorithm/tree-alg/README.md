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
