---
title: 移除整数n的第bit位函数
date: 2025-09-10
category: 其他
tags:
  - 算法
outline: deep
---

## code
- ```C++
	  int removebit(int n,int bit){
	  	int tail=n&((1ll>bit+1)<<bit;
	  	return tail|head;
	  }
	  ```