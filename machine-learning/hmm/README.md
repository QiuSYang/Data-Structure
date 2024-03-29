# 隐马尔科夫模型

## 隐马尔科夫模型的3个问题

1. **概率计算问题**，给定模型 gama = (A, B, Pai) 和观测序列 O = (o1, o2, ... , oT)，计算在模型gama下观测序列O出现的概率P(O|gama).

2. **学习问题**，已知观测序列 O = (o1, o2, ... , oT)，估计模型 gama = (A, B, Pai) 参数，使得在该模型下观测序列概率P(O|gama)最大，即用极大似然估计的方法估计参数。

3. **预测问题**，也称为解码(decoding)问题，已知模型 gama = (A, B, Pai) 和观测序列 O = (o1, o2, ... , oT)，求对给定观测序列条件概率P(I|Q)最大的状态序列 I = (i1, i2, ... , iT)，即给定观测序列，求最有可能的对应的状态序列。
