# 二叉树基础 --- 什么样的二叉树适合用数组来存储？

前面我们讲的都是线性表结构，栈、队列等等。今天我们讲一种非线性表结构，树。树这种数据结构比线性表的数据结构要复杂得多，内容也比较多，所以我会分四节来讲解。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/1.png)

带着问题学习，是最有效的学习方式之一。二叉树有哪几种存储方式？什么样的二叉树适合用数组来存储？

## 树(Tree)

首先来看，什么是“树”？再完备的定义，都没有图直观。所以我在图中画了几棵“树”。你来看看，这些“树”都有什么特征？

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/2.png)

你有没有发现，“树”这种数据结构真的很像我们现实生活中的“树”，这里面每个元素我们叫作“节点”；用来连线相邻节点之间的关系，我们叫作“父子关系”。

比如下面这幅图，A节点就是B节点的父节点，B节点是A节点的子节点。B、C、D这三个节点的父节点是同一个节点，所以它们之间互称为兄弟节点。我们把没有父节点的节点叫作根节点，也就是图中的节点E。我们把没有子节点的节点叫作叶子节点或者叶节点，比如图中的G、H、I、J、K、L都是叶子节点。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/3.png)

除此之外，关于“树”，还有三个比较相似的概念：高度（Height）、深度（Depth）、层（Level）。它们的定义是这样的：

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/4.png)

这三个概念的定义比较容易混淆，描述起来也比较空洞。我举个例子说明一下，你一看应该就能明白。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/5.png)

记这几个概念，我还有一个小窍门，就是类比“高度”“深度”“层”这几个名词在生活中的含义。

在我们的生活中，“高度”这个概念，其实就是从下往上度量，比如我们要度量第10层楼的高度、第13层楼的高度，起点都是地面。所以，树这种数据结构的高度也是一样，从最底层开始计数，并且计数的起点是0。

“深度”这个概念在生活中是从上往下度量的，比如水中鱼的深度，是从水平面开始度量的。所以，树这种数据结构的深度也是类似的，从根结点开始度量，并且计数起点也是0。

“层数”跟深度的计算类似，不过，计数起点是1，也就是说根节点的位于第1层。

## 二叉树(Binary Tree)

树结构多种多样，不过我们最常用还是二叉树。

二叉树，顾名思义，每个节点最多有两个“叉”，也就是两个子节点，分别是左子节点和右子节点。不过，二叉树并不要求每个节点都有两个子节点，有的节点只有左子节点，有的节点只有右子节点。我画的这几个都是二叉树。以此类推，你可以想象一下四叉树、八叉树长什么样子。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/6.png)

这个图里面，有两个比较特殊的二叉树，分别是编号2和编号3这两个。

其中，编号2的二叉树中，叶子节点全都在最底层，除了叶子节点之外，每个节点都有左右两个子节点，这种二叉树就叫作满二叉树。

编号3的二叉树中，叶子节点都在最底下两层，最后一层的叶子节点都靠左排列，并且除了最后一层，其他层的节点个数都要达到最大，这种二叉树叫作完全二叉树。

满二叉树很好理解，也很好识别，但是完全二叉树，有的人可能就分不清了。我画了几个完全二叉树和非完全二叉树的例子，你可以对比着看看。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/7.png)

满二叉树的特征非常明显，我们把它单独拎出来讲，这个可以理解。但是完全二叉树的特征不怎么明显啊，单从长相上来看，完全二叉树并没有特别特殊的地方啊，更像是“芸芸众树”中的一种.

那我们为什么还要特意把它拎出来讲呢？为什么偏偏把最后一层的叶子节点靠左排列的叫完全二叉树？如果靠右排列就不能叫完全二叉树了吗？这个定义的由来或者说目的在哪里？

要理解完全二叉树定义的由来，我们需要先了解，如何表示（或者存储）一棵二叉树？

想要存储一棵二叉树，我们有两种方法，一种是基于指针或者引用的二叉链式存储法，一种是基于数组的顺序存储法。

我们先来看比较简单、直观的链式存储法。从图中你应该可以很清楚地看到，每个节点有三个字段，其中一个存储数据，另外两个是指向左右子节点的指针。我们只要拎住根节点，就可以通过左右子节点的指针，把整棵树都串起来。这种存储方式我们比较常用。大部分二叉树代码都是通过这种结构来实现的。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/8.png)

我们再来看，基于数组的顺序存储法。我们把根节点存储在下标i = 1的位置，那左子节点存储在下标2 * i = 2的位置，右子节点存储在2 * i + 1 = 3的位置。以此类推，B节点的左子节点存储在2 * i = 2 * 2 = 4的位置，右子节点存储在2 * i + 1 = 2 * 2 + 1 = 5的位置。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/9.png)

我来总结一下，如果节点X存储在数组中下标为i的位置，下标为2 * i 的位置存储的就是左子节点，下标为2 * i + 1的位置存储的就是右子节点。反过来，下标为i/2的位置存储就是它的父节点。通过这种方式，我们只要知道根节点存储的位置（一般情况下，为了方便计算子节点，根节点会存储在下标为1的位置），这样就可以通过下标计算，把整棵树都串起来。

不过，我刚刚举的例子是一棵完全二叉树，所以仅仅“浪费”了一个下标为0的存储位置。如果是非完全二叉树，其实会浪费比较多的数组存储空间。你可以看我举的下面这个例子。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/10.png)

所以，如果某棵二叉树是一棵完全二叉树，那用数组存储无疑是最节省内存的一种方式。因为数组的存储方式并不需要像链式存储法那样，要存储额外的左右子节点的指针。这也是为什么完全二叉树会单独拎出来的原因，也是为什么完全二叉树要求最后一层的子节点都靠左的原因。

当我们讲到堆和堆排序的时候，你会发现，堆其实就是一种完全二叉树，最常用的存储方式就是数组。

## 二叉树的遍历

前面我讲了二叉树的基本定义和存储方法，现在我们来看二叉树中非常重要的操作，二叉树的遍历。这也是非常常见的面试题。

如何将所有节点都遍历打印出来呢？经典的方法有三种，前序遍历、中序遍历和后序遍历。其中，前、中、后序，表示的是节点与它的左右子树节点遍历打印的先后顺序。

    1. 前序遍历是指，对于树中的任意节点来说，先打印这个节点，然后再打印它的左子树，最后打印它的右子树。
    2. 中序遍历是指，对于树中的任意节点来说，先打印它的左子树，然后再打印它本身，最后打印它的右子树。
    3. 后序遍历是指，对于树中的任意节点来说，先打印它的左子树，然后再打印它的右子树，最后打印这个节点本身。
    
![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/11.png)

实际上，二叉树的前、中、后序遍历就是一个递归的过程。比如，前序遍历，其实就是先打印根节点，然后再递归地打印左子树，最后递归地打印右子树。

写递归代码的关键，就是看能不能写出递推公式，而写递推公式的关键就是，如果要解决问题A，就假设子问题B、C已经解决，然后再来看如何利用B、C来解决A。所以，我们可以把前、中、后序遍历的递推公式都写出来。

    前序遍历的递推公式：
    preOrder(r) = print r->preOrder(r->left)->preOrder(r->right)
    
    中序遍历的递推公式：
    inOrder(r) = inOrder(r->left)->print r->inOrder(r->right)
    
    后序遍历的递推公式：
    postOrder(r) = postOrder(r->left)->postOrder(r->right)->print r

有了递推公式，代码写起来就简单多了。这三种遍历方式的代码，我都写出来了，你可以看看。

    if (root == null) return;
        print root // 此处为伪代码，表示打印root节点
        preOrder(root->left);
        preOrder(root->right);
    }
    void inOrder(Node* root) {
        if (root == null) return;
        inOrder(root->left);
        print root // 此处为伪代码，表示打印root节点
        inOrder(root->right);
    }
    void postOrder(Node* root) {
        if (root == null) return;
        postOrder(root->left);
        postOrder(root->right);
        print root // 此处为伪代码，表示打印root节点
    }
    
二叉树的前、中、后序遍历的递归实现是不是很简单？你知道二叉树遍历的时间复杂度是多少吗？我们一起来看看。

从我前面画的前、中、后序遍历的顺序图，可以看出来，每个节点最多会被访问两次，所以遍历操作的时间复杂度，跟节点的个数n成正比，也就是说二叉树遍历的时间复杂度是O(n)。

## 解答开篇&内容小结

一种非线性表数据结构---树。关于树，有几个比较常用的概念你需要掌握，那就是：根节点、叶子节点、父节点、子节点、兄弟节点，还有节点的高度、深度、层数，以及树的高度。

我们平时最常用的树就是二叉树。二叉树的每个节点最多有两个子节点，分别是左子节点和右子节点。二叉树中，有两种比较特殊的树，分别是满二叉树和完全二叉树。满二叉树又是完全二叉树的一种特殊情况。

二叉树既可以用链式存储，也可以用数组顺序存储。**数组顺序存储的方式比较适合完全二叉树**，其他类型的二叉树用数组存储会比较浪费存储空间。除此之外，二叉树里非常重要的操作就是前、中、后序遍历操作，遍历的时间复杂度是O(n)，你需要理解并能用递归代码来实现。

# 二叉树基础 --- 有了如此高效的散列表，为什么还需要二叉树？

上一节我们学习了树、二叉树以及二叉树的遍历，今天我们再来学习一种特殊的的二叉树，**二叉查找树**。二叉查找树最大的特点就是，支持动态数据集合的**快速插入、删除、查找操作**。

之前说过，散列表也是支持这些操作的，并且散列表的这些操作比二叉查找树更高效，时间复杂度是O(1)。既然有了这么高效的散列表，使用二叉树的地方是不是都可以替换成散列表呢？有没有哪些地方是散列表做不了，必须要用二叉树来做的呢？

## 二叉查找树(Binary Search Tree)

二叉查找树是二叉树中最常用的一种类型，也叫**二叉搜索树**。顾名思义，二叉查找树是为了实现快速查找而生的。不过，它不仅仅支持快速查找一个数据，还支持快速插入、删除一个数据。它是怎么做到这些的呢？

这些都依赖于二叉查找树的特殊结构。二叉查找树要求，在树中的任意一个节点，其**左子树中的每个节点的值，都要小于这个节点的值**，而**右子树节点的值都大于这个节点的值**。 我画了几个二叉查找树的例子，你一看应该就清楚了。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/12.png)

前面我们讲到，二叉查找树支持快速查找、插入、删除操作，现在我们就依次来看下，这三个操作是如何实现的。

### 1. 二叉查找树的查找操作

首先，我们看如何在二叉查找树中查找一个节点。我们先取根节点，如果它等于我们要查找的数据，那就返回。如果要查找的数据比根节点的值小，那就在左子树中递归查找；如果要查找的数据比根节点的值大，那就在右子树中递归查找。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/13.png)

代码实现如下: 

    public class BinarySearchTree {
        private Node tree;
        public Node find(int data) {
            Node p = tree;
            while (p != null) {
                if (data < p.data) p = p.left;
                else if (data > p.data) p = p.right;
                else return p;
            }
            return null;
        }
        public static class Node {
            private int data;
            private Node left;
            private Node right;
            public Node(int data) {
                this.data = data;
            }
        }
    }

### 2. 二叉查找树的插入操作

二叉查找树的插入过程有点类似查找操作。新插入的数据一般都是在叶子节点上，所以我们只需要从根节点开始，依次比较要插入的数据和节点的大小关系。

如果要插入的数据比节点的数据大，并且节点的右子树为空，就将新数据直接插到右子节点的位置；如果不为空，就再递归遍历右子树，查找插入位置。同理，如果要插入的数据比节点数值小，并且节点的左子树为空，就将新数据插入到左子节点的位置；如果不为空，就再递归遍历左子树，查找插入位置。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/14.png)

代码实现如下:

    public void insert(int data) {
        if (tree == null) {
            tree = new Node(data);
            return;
        }
        Node p = tree;
        while (p != null) {
            if (data > p.data) {
                if (p.right == null) {
                    p.right = new Node(data);
                    return;
                }
                p = p.right;
                } else { // data < p.data
                    if (p.left == null) {
                    p.left = new Node(data);
                    return;
                }
                p = p.left;
            }
        }
    }

### 3. 二叉查找树的删除操作

二叉查找树的查找、插入操作都比较简单易懂，但是它的删除操作就比较复杂了 。针对要删除节点的子节点个数的不同，我们需要分三种情况来处理。

第一种情况是，如果要删除的节点没有子节点，我们只需要直接将父节点中，指向要删除节点的指针置为null。比如图中的删除节点55。

第二种情况是，如果要删除的节点只有一个子节点（只有左子节点或者右子节点），我们只需要更新父节点中，指向要删除节点的指针，让它指向要删除节点的子节点就可以了。比如图中的删除节点13。

第三种情况是，如果要删除的节点有两个子节点，这就比较复杂了。我们需要找到这个节点的右子树中的最小节点，把它替换到要删除的节点上。然后再删除掉这个最小节点，因为最小节点肯定没有左子节点（如果有左子结点，那就不是最小节点了），所以，我们可以应用上面两条规则来删除这个最小节点。比如图中的删除节点18。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/binary-tree/images/15.png)

代码实现：

    public void delete(int data) {
        Node p = tree; // p指向要删除的节点，初始化指向根节点
        Node pp = null; // pp记录的是p的父节点
        while (p != null && p.data != data) {
            pp = p;
            if (data > p.data) p = p.right;
            else p = p.left;
        }
        if (p == null) return; // 没有找到
        // 要删除的节点有两个子节点
        if (p.left != null && p.right != null) { // 查找右子树中最小节点
            Node minP = p.right;
            Node minPP = p; // minPP表示minP的父节点
            while (minP.left != null) {
                minPP = minP;
                minP = minP.left;
            }
            p.data = minP.data; // 将minP的数据替换到p中
            p = minP; // 下面就变成了删除minP了
            pp = minPP;
        }
        // 删除节点是叶子节点或者仅有一个子节点
        Node child; // p的子节点
        if (p.left != null) child = p.left;
        else if (p.right != null) child = p.right;
        else child = null;
        if (pp == null) tree = child; // 删除的是根节点
        else if (pp.left == p) pp.left = child;
        else pp.right = child;
    }

实际上，关于二叉查找树的删除操作，还有个非常简单、取巧的方法，就是单纯将要删除的节点标记为“已删除”，但是并不真正从树中将这个节点去掉。这样原本删除的节点还需要存储在内存中，比较浪费内存空间，但是删除操作就变得简单了很多。而且，这种处理方法也并没有增加插入、查找操作代码实现的难度。

### 4. 二叉查找树的其他操作

除了插入、删除、查找操作之外，二叉查找树中还可以支持快速地查找最大节点和最小节点、前驱节点和后继节点。这些操作我就不一一展示了。我会将相应的代码放到GitHub上，你可以自己先实现一下，然后再去上面看。

二叉查找树除了支持上面几个操作之外，还有一个重要的特性，就是**中序遍历**二叉查找树，可以输出有序的数据序列，时间复杂度是O(n)，非常高效。因此，二叉查找树也叫作二叉排序树。

## 支持重复数据的二叉查找树

