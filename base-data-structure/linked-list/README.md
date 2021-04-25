链表

1.如何通过链表实现LRU缓存淘汰算法？缓存是一种提高数据读取性能的技术，在硬件设计、软件开发中都有着非常广泛的应用，比如常见的CPU缓存、数据库缓存、浏览器缓存等等。

缓存的大小有限，当缓存被用满时，哪些数据应该被清理出去，哪些数据应该被保留？这就需要缓存淘汰策略来决定。常见的策略有三种：先进先出策略FIFO（First In，First Out）、最少使用策略LFU（Least Frequently Used）、最近最少使用策略LRU（Least Recently Used）。

2.链表与数组之间的区别？

从图中我们看到，数组需要一块连续的内存空间来存储，对内存的要求比较高。如果我们申请一个100MB大小的数组，当内存中没有连续的、足够大的存储空间时，即便内存的剩余总可用空间大于100MB，仍然会申请失败。

而链表恰恰相反，它并不需要一块连续的内存空间，它通过“指针”将一组零散的内存块串联起来使用，所以如果我们申请的是100MB大小的链表，根本不会有问题。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/1.png)

链表结构五花八门，今天我重点给你介绍三种最常见的链表结构，它们分别是：单链表、双向链表和循环链表。我们首先来看最简单、最常用的单链表。

3.单链表

链表通过指针将一组零散的内存块串联在一起。其中，我们把内存块称为链表的“结点”。为了将所有的结点串起来，每个链表的结点除了存储数据之外，还需要记录链上的下一个结点的地址。如图所示，我们把这个记录下个结点地址的指针叫作后继指针next。仅包含后继指针的叫做“单链表”。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/2.png)

从单链表图中，你应该可以发现，其中有两个结点是比较特殊的，它们分别是第一个结点和最后一个结点。我们习惯性地把第一个结点叫作头结点，把最后一个结点叫作尾结点。其中，头结点用来记录链表的基地址。有了它，我们就可以遍历得到整条链表。而尾结点特殊的地方是：指针不是指向下一个结点，而是指向一个空地址NULL，表示这是链表上最后一个结点。

与数组一样，链表也支持数据的查找、插入和删除操作。

在进行数组的插入、删除操作时，为了保持内存数据的连续性，需要做大量的数据搬移，所以时间复杂度是O(n)。而在链表中插入或者删除一个数据，我们并不需要为了保持内存的连续性而搬移结点，因为链表的存储空间本身就不是连续的。所以，在链表中插入和删除一个数据是非常快速的。

针对链表的插入和删除操作，我们只需要考虑相邻结点的指针改变，所以对应的时间复杂度是O(1)。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/3.png)

链表基本操作有利就有弊。链表要想随机访问第k个元素，就没有数组那么高效了。因为链表中的数据并非连续存储的，所以无法像数组那样，根据首地址和下标，通过寻址公式就能直接计算出对应的内存地址，而是需要根据指针一个结点一个结点地依次遍历，直到找到相应的结点。

你可以把链表想象成一个队伍，队伍中的每个人都只知道自己后面的人是谁，所以当我们希望知道排在第k位的人是谁的时候，我们就需要从第一个人开始，一个一个地往下数。所以，链表随机访问的性能没有数组好，需要O(n)的时间复杂度。

4.循环链表

循环链表是一种特殊的单链表。实际上，循环链表也很简单。它跟单链表唯一的区别就在尾结点。我们知道，单链表的尾结点指针指向空地址，表示这就是最后的结点了。而循环链表的尾结点指针是指向链表的头结点。从我画的循环链表图中，你应该可以看出来，它像一个环一样首尾相连，所以叫作“循环”链表。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/4.png)

和单链表相比， 循环链表的优点是从链尾到链头比较方便。当要处理的数据具有环型结构特点时，就特别适合采用循环链表。比如著名的[约瑟夫问题]。尽管用单链表也可以实现，但是用循环链表实现的话，代码就会简洁很多。

5.双向链表

双向链表，顾名思义，它支持两个方向，每个结点不止有一个后继指针next指向后面的结点，还有一个前驱指针prev指向前面的结点。

图中可以看出来，双向链表需要额外的两个空间来存储后继结点和前驱结点的地址。所以，如果存储同样多的数据，双向链表要比单链表占用更多的内存空间。虽然两个指针比较浪费存储空间，但可以支持双向遍历，这样也带来了双向链表操作的灵活性。那相比单链表，双向链表适合解决哪种问题呢？

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/5.png)

从结构上来看，双向链表可以支持O(1)时间复杂度的情况下找到前驱结点，正是这样的特点，也使双向链表在某些情况下的插入、删除等操作都要比单链表简单、高效。

在实际的软件开发中，从链表中删除一个数据无外乎这两种情况：

    删除结点中“值等于某个给定值”的结点；
    删除给定指针指向的结点。

对于第一种情况，不管是单链表还是双向链表，为了查找到值等于给定值的结点，都需要从头结点开始一个一个依次遍历对比，直到找到值等于给定值的结点，然后再通过我前面讲的指针操作将其删除。

尽管单纯的删除操作时间复杂度是O(1)，但遍历查找的时间是主要的耗时点，对应的时间复杂度为O(n)。根据时间复杂度分析中的加法法则，删除值等于给定值的结点对应的链表操作的总时间复杂度为O(n)。

对于第二种情况，我们已经找到了要删除的结点，但是删除某个结点q需要知道其前驱结点，而单链表并不支持直接获取前驱结点，所以，为了找到前驱结点，我们还是要从头结点开始遍历链表，直到p->next=q，说明p是q的前驱结点。

但是对于双向链表来说，这种情况就比较有优势了。因为双向链表中的结点已经保存了前驱结点的指针，不需要像单链表那样遍历。所以，针对第二种情况，单链表删除操作需要O(n)的时间复杂度，而双向链表只需要在O(1)的时间复杂度内就搞定了！

同理，如果我们希望在链表的某个指定结点前面插入一个结点，双向链表比单链表有很大的优势。双向链表可以在O(1)时间复杂度搞定，而单向链表需要O(n)的时间复杂度。你可以参照我刚刚讲过的删除操作自己分析一下。

除了插入、删除操作有优势之外，对于一个有序链表，双向链表的按值查询的效率也要比单链表高一些。因为，我们可以记录上次查找的位置p，每次查询时，根据要查找的值与p的大小关系，决定是往前还是往后查找，所以平均只需要查找一半的数据。

6.循环双向链表

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/6.png)

7.数组 VS 链表

数组和链表是两种截然不同的内存组织方式。正是因为内存存储的区别，它们插入、删除、随机访问操作的时间复杂度正好相反。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/7.png)

不过，数组和链表的对比，并不能局限于时间复杂度。而且，在实际的软件开发中，不能仅仅利用复杂度分析就决定使用哪个数据结构来存储数据。

数组简单易用，在实现上使用的是连续的内存空间，可以借助CPU的缓存机制，预读数组中的数据，所以访问效率更高。而链表在内存中并不是连续存储，所以对CPU缓存不友好，没办法有效预读。

数组的缺点是大小固定，一经声明就要占用整块连续内存空间。如果声明的数组过大，系统可能没有足够的连续内存空间分配给它，导致“内存不足（out ofmemory） ”。如果声明的数组过小，则可能出现不够用的情况。这时只能再申请一个更大的内存空间，把原数组拷贝进去，非常费时。链表本身没有大小的限制，天然地支持动态扩容，我觉得这也是它与数组最大的区别。

8.如何基于链表实现LRU缓存淘汰算法？

维护一个有序单链表，越靠近链表尾部的结点是越早之前访问的。当有一个新的数据被访问时，我们从链表头开始顺序遍历链表。

1.如果此数据之前已经被缓存在链表中了，我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。

2.如果此数据没有在缓存链表中，又可以分为两种情况：

    如果此时缓存未满，则将此结点直接插入到链表的头部；
    如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。

这样我们就用链表实现了一个LRU缓存，是不是很简单？

现在我们来看下m缓存访问的时间复杂度是多少。因为不管缓存有没有满，我们都需要遍历一遍链表，所以这种基于链表的实现思路，缓存访问的时间复杂度为O(n)。

实际上，我们可以继续优化这个实现思路，比如引入散列表（Hash table）来记录每个数据的位置，将缓存访问的时间复杂度降到O(1)。因为要涉及我们还没有讲到的数据结构，所以这个优化方案，我现在就不详细说了，等讲到散列表的时候，我会再拿出来讲。

除了基于链表的实现思路，实际上还可以用数组来实现LRU缓存淘汰策略。

9.理解指针或引用的含义

对于指针的理解，你只需要记住下面这句话就可以了：

    将某个变量赋值给指针，实际上就是将这个变量的地址赋值给指针，或者反过来说，指针中存储了这个变量的内存地址，指向了这个变量，通过指针就能找到这个变量。
    在编写链表代码的时候，我们经常会有这样的代码：p->next=q。这行代码是说，p结点中的next指针存储了q结点的内存地址。
    还有一个更复杂的，也是我们写链表代码经常会用到的：p->next=p->next->next。这行代码表示，p结点的next指针存储了p结点的下下一个结点的内存地址。

10.警惕指针丢失和内存泄漏

指针往往都是怎么弄丢的呢？我拿单链表的插入操作为例来给你分析一下。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/8.png)

如图所示，我们希望在结点a和相邻的结点b之间插入结点x，假设当前指针p指向结点a。如果我们将代码实现变成下面这个样子，就会发生指针丢失和内存泄露。
    
    p->next = x; // 将p的next指针指向x结点；
    x->next = p->next; // 将x的结点的next指针指向b结点；

初学者经常会在这儿犯错。p->next指针在完成第一步操作之后，已经不再指向结点b了，而是指向结点x。第2行代码相当于将x赋值给x->next，自己指向自己。因此，整个链表也就断成了两半，从结点b往后的所有结点都无法访问到了。

对于有些语言来说，比如C语言，内存管理是由程序员负责的，如果没有手动释放结点对应的内存空间，就会产生内存泄露。所以，我们插入结点时，一定要注意操作的顺序，要先将结点x的next指针指向结点b，再把结点a的next指针指向结点x，这样才不会丢失指针，导致内存泄漏。所以，对于刚刚的插入代码，我们只需要把第1行和第2行代码的顺序颠倒一下就可以了。

同理，删除链表结点时，也一定要记得手动释放内存空间，否则，也会出现内存泄漏的问题。

11.利用哨兵简化实现难度

还记得如何表示一个空链表吗？head=null表示链表中没有结点了。其中head表示头结点指针，指向链表中的第一个结点。

如果我们引入哨兵结点，在任何时候，不管链表是不是空，head指针都会一直指向这个哨兵结点。我们也把这种有哨兵结点的链表叫带头链表。相反，没有哨兵结点的链表就叫作不带头链表。

我画了一个带头链表，你可以发现，哨兵结点是不存储数据的。因为哨兵结点一直存在，所以插入第一个结点和插入其他结点，删除最后一个结点和删除其他结点，都可以统一为相同的代码实现逻辑了。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/9.png)

实际上，这种利用哨兵简化编程难度的技巧，在很多代码实现中都有用到，比如插入排序、归并排序、动态规划等。这些内容我们后面才会讲，现在为了让你感受更深，我再举一个非常简单的例子。代码我是用C语言实现的，不涉及语言方面的高级语法，很容易看懂，你可以类比到你熟悉的语言。

题目：在数组a中，查找key，返回key所在的位置，其中，n表示数组a的长度。例如：a = {4, 2, 3, 5, 9, 6} n=6 key = 7

代码一：
 
    int find(char* a, int n, char key) {
     // 边界条件处理，如果a为空，或者n<=0，说明数组中没有数据，就不用while循环比较了
     if(a == null || n <= 0) {
        return -1;
     }
    
     int i = 0;
     // 这里有两个比较操作：i<n和a[i]==key.
     while (i < n) {
        if (a[i] == key) {
            return i;
        }
        ++i;
     }
    
     return -1;
    }

代码二：可读性差

    int find(char* a, int n, char key) {
     if(a == null || n <= 0) {
        return -1;
     }
    
     // 这里因为要将a[n-1]的值替换成key，所以要特殊处理这个值
     if (a[n-1] == key) {
        return n-1;
     }
    
     // 把a[n-1]的值临时保存在变量tmp中，以便之后恢复。tmp=6。
     // 之所以这样做的目的是：希望find()代码不要改变a数组中的内容
     char tmp = a[n-1];
     // 把key的值放到a[n-1]中，此时a = {4, 2, 3, 5, 9, 7}
     a[n-1] = key;
    
     int i = 0;
     // while 循环比起代码一，少了i<n这个比较操作
     while (a[i] != key) {
        ++i;
     }
    
     // 恢复a[n-1]原来的值,此时a= {4, 2, 3, 5, 9, 6}
     a[n-1] = tmp;
    
     if (i == n-1) {
     // 如果i == n-1说明，在0...n-2之间都没有key，所以返回-1
        return -1;
     } else {
     // 否则，返回i，就是等于key值的元素的下标
        return i;
     }
    }
    
对比两段代码，在字符串a很长的时候，比如几万、几十万，你觉得哪段代码运行得更快点呢？答案是代码二，因为两段代码中执行次数最多就是while循环那一部分。第二段代码中，我们通过一个哨兵a[n-1] = key，成功省掉了一个比较语句i<n，不要小看这一条语句，当累积执行万次、几十万次时，累积的时间就很明显了。

12.重点留意边界条件处理

要实现没有Bug的链表代码，一定要在编写的过程中以及编写完成之后，检查边界条件是否考虑全面，以及代码在边界条件下是否能正确运行。

我经常用来检查链表代码是否正确的边界条件有这样几个：
    
    1. 如果链表为空时，代码是否能正常工作？
    2. 如果链表只包含一个结点时，代码是否能正常工作？
    3. 如果链表只包含两个结点时，代码是否能正常工作？
    4. 代码逻辑在处理头结点和尾结点的时候，是否能正常工作？
    
当你写完链表代码之后，除了看下你写的代码在正常的情况下能否工作，还要看下在上面我列举的几个边界条件下，代码仍然能否正确工作。如果这些边界条件下都没有问题，那基本上可以认为没有问题了。
当然，边界条件不止我列举的那些。针对不同的场景，可能还有特定的边界条件，这个需要你自己去思考，不过套路都是一样的

13.举例画图，辅助思考

对于稍微复杂的链表操作，比如前面我们提到的单链表反转，指针一会儿指这，一会儿指那，一会儿就被绕晕了。总感觉脑容量不够，想不清楚。所以这个时候就要使用大招了，举例法和画图法。

你可以找一个具体的例子，把它画在纸上，释放一些脑容量，留更多的给逻辑思考，这样就会感觉到思路清晰很多。比如往单链表中插入一个数据这样一个操作，我一般都是把各种情况都举一个例子，画出插入前和插入后的链表变化，如图所示：

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/linked-list/images/10.png)

看图写代码，是不是就简单多啦？而且，当我们写完代码之后，也可以举几个例子，画在纸上，照着代码走一遍，很容易就能发现代码中的Bug。

13.多写多练，没有捷径

精选了5个常见的链表操作。你只要把这几个操作都能写熟练，不熟就多写几遍，我保证你之后再也不会害怕写链表代码。
    
    1. 单链表反转
    2. 链表中环的检测 --- 快慢指针实现，快指针每次走两步，慢指针走一步，看是否会相遇
    3. 两个有序的链表合并
    4. 删除链表倒数第n个结点 --- 快慢指针实现，快指针从链头先走n步，之后快慢指针同事移动，快指针到达链尾，慢指针刚好到达倒数n个节点(因为快慢指针刚好相差n个节点)
    5. 求链表的中间结点 --- 快慢指针实现，快指针步长为2，慢指针步长为1，快指针走到链尾，慢指针就指向链中
    

## LeetCode-206. 反转链表

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseList(self, head: ListNode) -> ListNode:
            """使用递归实现链表反转"""
            if head is None:
                return head 
            if head.next is None:
                return head 
            # 细化为单个节点反转
            lasted = self.reverseList(head.next)  # 反转当前头结点之后的所有节点
            head.next.next = head  # 后一个节点的next节点等于前一个节点
            head.next = None  # 断开连接, 原来前一个节点与后一个节点断开连接
    
            return lasted 
        
        def _reverseList(self, head: ListNode) -> ListNode:
            """使用循环的方式"""
            if head is None:
                return head 
            
            pre, cur, nxt = None, head, head
            while cur is not None:
                nxt = cur.next
                # 逐个结点反转
                cur.next = pre 
                # 更新指针位置
                pre = cur 
                cur = nxt
            
            return pre 
            
## LeetCode-25. K 个一组翻转链表

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
            if head is None: return None;
            # 区间 [a, b) 包含 k 个待反转元素
            a = b = head;
            for i in range(k):
                # 不足 k 个，不需要反转，base case
                if b is None:
                     return head
                b = b.next
            # 反转前 k 个元素
            newHead = self.reverse(a, b);
            # 递归反转后续链表并连接起来
            a.next = self.reverseKGroup(b, k);
            return newHead;
    
        def reverse(self, a: ListNode, b: ListNode) -> ListNode:
            """反转一个区间内的数组"""
            pre = None
            cur = a
            nxt = a
            # while 终止的条件改一下就行了
            while cur != b:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # 返回反转后的头结点
            return pre
            
## LeetCode-92.反转链表II --- 规定范围节点反转

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        successor = ListNode()  # 后驱节点
        # def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        #     """使用循环的方式反转一个链表区间"""
        #     if head is None:
        #         return head 
            
        #     # 寻找三个节点区间
        #     index = 1 
        #     left_node, right_node = None, None 
        #     temp = head 
        #     result = ListNode()
        #     temp_result = result
        #     while temp is not None:
        #         if index < left:
        #             temp_result.next = temp
        #             temp_result = temp  # 指针移动
        #         elif index == left:
        #             left_node = temp
        #         elif index == right + 1:
        #             right_node = temp
        #         index += 1
        #         temp = temp.next 
            
        #     pre, cur, nxt = None, left_node, left_node
        #     # print(right_node.next)
        #     while cur is not right_node:
        #         # print(cur)
        #         nxt = cur.next
        #         # 逐个结点反转
        #         cur.next = pre 
        #         # 更新指针位置
        #         pre = cur 
        #         cur = nxt
            
        #     # 两端拼接
        #     left_node.next = right_node
        #     temp_result.next = pre 
    
        #     return result.next 
    
        def reverse_n(self, head: ListNode, n: int) -> ListNode:
            """反转前n个节点"""
            # 反转以 head 为起点的 n 个节点，返回新的头结点
            if n == 1:
                self.successor = head.next
                return head   # 最后一个节点
            
            lasted = self.reverse_n(head.next, n - 1)
            head.next.next = head  # 两个节点对调
            # 让反转之后的 head 节点和后面的节点连起来
            head.next = self.successor 
    
            return lasted 
    
        def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
            """使用递归方式反转规定范围内的节点"""
            if head is None:
                return head 
            if left == 1:
                # 左节点到达作为头节点
                return self.reverse_n(head, right)
            
            # 寻找以Left位置为head node 子链表, 转换为一个反转前N个节点的问题
            head.next = self.reverseBetween(head.next, left-1, right-1)
    
            return head 
            
## LeetCode-9.回文数 --- 双指针法

    class Solution:
        def isPalindrome(self, x: int) -> bool:
            """双指针判断是否为回文字符"""
            x = str(x)
            left, right = 0, len(x)-1
            while left < right:
                if x[left] != x[right]:
                    return False
                left += 1 
                right -= 1
    
            return True 

## 链表其实也可以有前序遍历和后序遍历

    void traverse(ListNode head) {
        // 前序遍历代码
        if head is None:
            return 
        print(head.val)
        traverse(head.next);
    }

    /* 倒序打印单链表中的元素值 */
    void traverse(ListNode head) {
        if (head == null) return;
        traverse(head.next);
        // 后序遍历代码
        print(head.val);
    }

模仿双指针实现回文判断的功能

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        left = ListNode()  # 左指针
        def isPalindrome(self, head: ListNode) -> bool:
            if head is None:
                return True 
            self.left = head 
            return self.traverse(head)
    
        def traverse(self, right: ListNode) -> bool:
            """链表逆序访问"""
            if right is None: return True 
            res = self.traverse(right.next)
    
            res = res and right.val == self.left.val
            self.left = self.left.next 
    
            return res 

这么做的核心逻辑是什么呢？**实际上就是把链表节点放入一个栈，然后再拿出来，这时候元素顺序就是反的**，只不过我们利用的是递归函数的堆栈而已。

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def isPalindrome(self, head: ListNode) -> bool:
            if head is None:
                return True 
            # 先通过「双指针技巧」中的快慢指针来找到链表的中点
            slow = fast = head 
            while fast is not None and fast.next is not None:
                slow = slow.next  # 慢指针走一步
                fast = fast.next.next  # 快指针走两步
            if fast is not None:
                # 如果fast指针没有指向null，说明链表长度为奇数，slow还要再前进一步
                slow = slow.next 
            # print(slow)
            
            # 从slow开始反转后面的链表，现在就可以开始比较回文串了
            left = head 
            right = self.reverse(slow)
            #print(right)
            while right is not None:
                if left.val != right.val:
                    return False 
                left = left.next 
                right = right.next 
            
            return True 
    
        def reverse(self, head: ListNode) -> ListNode:
            """反转链表"""
            pre, cur = None, head
            while cur is not None:
                # 指针移动
                nxt = cur.next
                cur.next = pre 
                # 指针转向
                pre = cur
                cur = nxt   
    
            return pre      

算法总体的时间复杂度 O(N)，空间复杂度 O(1)，已经是最优的了。

我知道肯定有读者会问：这种解法虽然高效，但破坏了输入链表的原始结构，能不能避免这个瑕疵呢？

其实这个问题很好解决，关键在于得到p, q这两个指针位置：

![image](images/11.jpg)

这样，只要在函数 return 之前加一段代码即可恢复原先链表顺序：

    p.next = self.reverse(q)
