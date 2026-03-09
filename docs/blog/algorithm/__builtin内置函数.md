---
title: __builtin内置函数
date: 2025-12-20
category: 数学
tags:
  - 算法
outline: deep
---

### __builtin_popcount(x)
- 返回x的二进制表示中1的个数。
- >> int count = __builtin_popcount(15); 
输出:4
15 = 1111 , 1的个数位4
### __builtin_clz(x)/__builtin_clzll(x)
- 返回x的二进制表示中从最高位开始连续0的个数，如果x的值为0，则返回所在类型的位宽。
- ==63 - 前导零个数 = 最高有效位下标 (MSB）==
- >> int count = __builtin_clz(8);
输出:28
8 = 0000 0000 0000 0000 0000 0000 0000 1000 , 整型(int)为32位,有28个前导0
### __builtin_ctz(x)/__builtin_ctzll(x)
- 返回x的二进制表示中从最低位开始连续0的个数，如果x的值为0，则返回所在类型的位宽。
- >> int count = __builtin_ctz(8); 
输出:3
8 = 1000
###  __builtin_sqrt
- 那么他们跟 sqrt() 有什么区别呢？做个小测试:  比较耗时:
sqrt: 约 3700 ms , __builtin_sqrt( ): 约 330 ms
快了接近10倍！
__builtin_sqrt是double的精度
- >> cout<< __builtin_sqrt(15) <<endl ;
输出: 3.87298
-