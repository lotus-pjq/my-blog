---
title: 勒让德公式(Legendre)
date: 2026-03-09
category: 数论
tags:
  - 算法
description: 勒让德公式(Legendre)相关的算法笔记和代码模板
---

## log(n)求阶乘 n! 中含有的素数 p 的幂次：
- 对于阶乘 \( n! \) 中含有的素数 \( p \) 的幂次 \( \nu_p(n!) \) 为：
  \[
  \nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \frac{n}{p^i} \right\rfloor = \frac{n - S_p(n)}{p - 1},
  \]
  其中，\( S_p(n) \) 为 \( p \) 进制下 \( n \) 的各个数位的和。特别地，阶乘中 2 的幂次是 \( \nu_2(n!) = n - S_2(n) \)。
- ```C++
  int legendre(int n,int p){
  	int cnt=0;
  	do{
  		n/=p;
  		cnt+=n;
  	}while(n);
  	return cnt;
  }
  ```
-