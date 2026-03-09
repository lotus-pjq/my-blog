---
title: 移除整数n的第bit位函数
date: 2026-03-09
category: 其他
tags:
  - 算法
description: 移除整数n的第bit位函数相关的算法笔记和代码模板
---

## code
	- ```C++
	  int removebit(int n,int bit){
	  	int tail=n&((1ll<<bit)-1);
	  	int head=(n>>bit+1)<<bit;
	  	return tail|head;
	  }
	  ```