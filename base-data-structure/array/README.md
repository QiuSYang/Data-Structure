数组--》数组（Array）是一种线性表数据结构。它用一组连续的内存空间，来存储一组具有相同类型的数据。

1. 第一是线性表（Linear List）。顾名思义，线性表就是数据排成像一条线一样的结构。每个线性表上的数据最多只有前和后两个方向。其实除了数组，链表、队列、栈等也是线性表结构。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/array/images/1.png)

而与它相对立的概念是非线性表，比如二叉树、堆、图等。之所以叫非线性，是因为，在非线性表中，数据之间并不是简单的前后关系。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/array/images/2.png)

2. 第二个是“连续的内存空间”和“相同类型的数据”。正是因为这两个限制，它才有了一个堪称“杀手锏”的特性： “随机访问”。但有利就有弊，这两个限制也让数组的很多操作变得非常低效，比如要想在数组中删除、插入一个数据，为了保证连续性，就需要做大量的数据搬移工作。

3. 说到数据的访问，那你知道数组是如何实现根据下标随机访问数组元素的吗？
我们拿一个长度为10的int类型的数组int[] a = new int[10]来举例。在我画的这个图中，计算机给数组a[10]，分配了一块连续内存空间1000～1039，其中，内存块的首地址为base_address = 1000。

![Image text](https://github.com/QiuSYang/Data-Structure/blob/master/base-data-structure/array/images/3.png)

我们知道，计算机会给每个内存单元分配一个地址，计算机通过地址来访问内存中的数据。当计算机需要随机访问数组中的某个元素时，它会首先通过下面的寻址公式，计算出该元素存储的内存地址：
    
    a[i]_address = base_address + i * data_type_size
