---
title: Multi-SG
date: 2025-08-07
category: 博弈论
tags:
  - 博弈论
  - SG函数
  - 模板
outline: deep
---

tags:: #算法/博弈论 #算法/SG函数 #模板

- [博弈论进阶之Multi-SG - 自为风月马前卒 - 博客园](https://www.cnblogs.com/zwfymqz/p/8469862.html)
- ### Multi-SG游戏:
- #### 定义：
	  1，在符合拓扑原则的前提下，一个单一游戏的后继可以为多个单一游戏
	  2，其他规则与SG游戏相同
- #### 求解：
	  可以通过将SG函数适当变形来解决。只需要证明：我们依然可以用SG函数来定义局面。
	  因为局面在游戏树中满足拓扑关系(无环)，所以我们可以根据拓扑关系用数学归纳法来证明。
- 对于一个状态来说，不同的划分方法会产生多个不同的后继，而在一个后继中可能含有多个独立的游戏
- ==一个后继状态的SG值即为后继状态中独立游戏的异或和==
- 该状态的SG值即为后继状态的SG值中未出现过的最小值
- ---
- ### Multi-Nim模型：- 从最简单的Nim模型开始它的定义是这样的：
	  有n堆石子，两个人可以从任意一堆石子中拿任意多个石子(不能不拿)**或把一堆数量不少于2石子分为两堆不为空的石子**，没法拿的人失败。问谁会胜利
- ---
- 这个问题的本质还是Nim游戏，可以利用SG定理来解释
	  通过观察不难不发现，操作一与普通的Nim游戏等价
	  操作二实际上是将一个游戏分解为两个游戏，根据SG定理，我们可以通过异或运算把两个游戏连接到一起，作为一个后继状态
- 煮个栗子：
- SG(3)的后继状态有{(0),(1),(2),(1,2)}他们的SG值分别为{0,1,2,3}，因此SG(3)=mex{0,1,2,3}=4
- 归纳易得： 
- ---
- ### POJ 2311.切割游戏- 
- **比较有意思的一道题目，如果你知道什么叫Multi-Nim，那么这道题就比较简单了**
- **最关键的地方就是**
- **一个游戏的SG函数为后继状态异或和的mex**
- **注意边长需要从2枚举，否则2*2这个状态会挂掉**
- ```C++
	  #include
	  #include
	  using namespace std;
	  const int MAXN=233;
	  int read()
	  {
	      char c=getchar();int x=0,f=1;
	      while(c'9'){if(c=='-')f=-1;c=getchar();}
	      while(c>='0'&&c
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  #define clr(f,n) memset(f,0,sizeof(int)*(n))
	  #define cpy(f,g,n) memcpy(f,g,sizeof(int)*(n))
	  #define INF 0x3f3f3f3f3f3f3f3f
	  #define rep(i,j,k) for (int i=j;i=k;--i)
	  //#define mid (l+r>>1)
	  //#define ls x st;
	  	for(int k=2;k>t>>f;
	  	for(int i=0;i>n;
	  		int ans=0;
	  		for(int i=1;i>a[i];}
	  		for(int i=1;i<=n;i++) ans^=SG(a[i]);
	  		if(ans) cout<<1<<" ";
	  		else cout<<0<<" ";
	      }
	      return 0;
	  }
	  ```