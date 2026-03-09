---
title: 树形DP
date: 2026-03-09
category: 图论
tags:
  - 算法
description: 树形DP相关的算法笔记和代码模板
---

### 实现形式
	- 树形dp的主要实现形式是dfs，在dfs中dp。
	- 主要的实现形式是==dp[i][j][0/1]==，
	  > $i$ : 以i为根的子树，
	  $j$ : 表示在以i为根的子树中选择j子节点，
	  $0/1$ : 0表示这个节点不选，1表示选择这个节点。
	  有的时候$j$或$0/1$这一维可以压掉
- ### 基本的dp方程
	- #### 选择节点类
		- $dp[i][0]=dp[j][1]$
		- $dp[i][1]=max/min(dp[j][1],dp[j][0])$
	- #### 树形背包
		- $dp[v][k]=dp[u][k]+val$
		- $dp[u][k]=max(dp[u][k],dp[v][k-1])$
- ### P1352 没有上司的舞会
	- 题目：
		- ## P1352 没有上司的舞会
		- ## 题目描述
		  某大学有 $n$ 个职员，编号为 $1\ldots n$。
		  他们之间有从属关系，也就是说他们的关系就像一棵以校长为根的树，父结点就是子结点的直接上司。
		  现在有个周年庆宴会，宴会每邀请来一个职员都会增加一定的快乐指数 $r_i$，但是呢，如果某个职员的直接上司来参加舞会了，那么这个职员就无论如何也不肯来参加舞会了。
		  所以，请你编程计算，邀请哪些职员可以使快乐指数最大，求最大的快乐指数。
		- ## 输入格式
		  输入的第一行是一个整数 $n$。
		  第 $2$ 到第 $(n + 1)$ 行，每行一个整数，第 $(i+1)$ 行的整数表示 $i$ 号职员的快乐指数 $r_i$。
		  第 $(n + 2)$ 到第 $2n$ 行，每行输入一对整数 $l, k$，代表 $k$ 是 $l$ 的直接上司。
		- ## 输出格式
		  输出一行一个整数代表最大的快乐指数。
		- ### 输入 1
		  ```
		  7
		  1
		  1
		  1
		  1
		  1
		  1
		  1
		  1 3
		  2 3
		  6 4
		  7 4
		  4 5
		  3 5
		  ```
		- ### 输出 1
		  ```
		  5
		  ```
		- #### 数据规模与约定
		  对于 $100\%$ 的数据，保证 $1\leq n \leq 6 \times 10^3$，$-128 \leq r_i\leq 127$，$1 \leq l, k \leq n$，且给出的关系一定是一棵树。
	- Code：
		- ```C++
		  //P1352 没有上司的舞会
		  #include<bits/stdc++.h>
		  using namespace std;
		  const int N=6e3+5;
		  int a[N],fa[N];
		  int n,m,l,k,root;
		  int dp[N][2];
		  //dp[x][1/0]:以x为根节点的子树并且(1:包括x/0:不包含)的总快乐指数
		  vector<int> e[N];
		  void dfs(int x){
		  	dp[x][1]=a[x];
		      for(auto u:e[x]){
		          dfs(u);
		          dp[x][0]+=max(dp[u][0],dp[u][1]);
		          dp[x][1]+=max(dp[u][0],0);
		      }
		  }
		  signed main(){
		      cin>>n;
		      for(int i=1;i<=n;i++) cin>>a[i];
		      for(int i=1;i<=n-1;i++){    
		          cin>>l>>k;
		          fa[l]=k;
		          e[k].push_back(l);
		      }
		  	for(int i=1;i<=n;i++) if(!fa[i]){root=i;break;}
		  	dfs(root);
		  	cout<<max(dp[root][0],dp[root][1]); 
		  }
		  ```
- ### P2014 [CTSC1997] 选课 #树上背包
	- 题目：
		- ## P2014 [CTSC1997] 选课
		- ## 题目描述
		  在大学里每个学生，为了达到一定的学分，必须从很多课程里选择一些课程来学习，在课程里有些课程必须在某些课程之前学习，如高等数学总是在其它课程之前学习。现在有 $N$ 门功课，每门课有若干学分，分别记作 $s_1,s_2,\cdots,s_N$，每门课有一门或没有直接先修课（若课程 $a$ 是课程 $b$ 的先修课即只有学完了课程 $a$，才能学习课程 $b$）。一个学生要从这些课程里选择 $M$ 门课程学习，问他能获得的最大学分是多少？
		- ## 输入格式
		  第一行有两个整数 $N$，$M$ 用空格隔开 $(1 \leq N \leq 300$ , $1 \leq M \leq 300)$。
		  接下来的 $N$ 行,第 $i+1$ 行包含两个整数 $k_i$ 和 $s_i$, $k_i$ 表示第 $i$ 门课的直接先修课，$s_i$ 表示第 $i$ 门课的学分。若 $k_i=0$ 表示没有直接先修课 $(0 \leq {k_i} \leq N$,$1 \leq {s_i} \leq 20)$。
		- ## 输出格式
		  只有一行，选 $M$ 门课程的最大学分。
		- ### 输入 1
		  ```
		  7  4
		  2  2
		  0  1
		  0  4
		  2  1
		  7  1
		  7  6
		  2  2
		  ```
		- ### 输出 1
		  ```
		  13
		  ```
	- 思路
		-
		  > 设计状态：dp[u][i][j]表示节点u的前i个子节点，限重为j能得到的最大权值和（价值和）
		  像01背包一样压缩空间，得到：f[u][j]:以u为根的子树，选了j门课的最大学分
		  递推起点：f[u][1]=w[u];
		  f[u][j]=max(f[u][j],f[u][j-k]+f[v][k])
		  01背包，逆序枚举 j:m+1->1, k:1->j-1
		  0号点的为必选点，所以共选 m+1门
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=3e3+5;
		  int n,m;
		  int w[N],f[N][N],siz[N];
		  //f[u][j]:以u为根的子树，选了j门课的最大学分
		  //递推起点：f[u][1]=w[u];
		  //f[u][j]=max(f[u][j],f[u][j-k]+f[v][k])
		  //01背包，逆序枚举 j:m+1->1, k:1->j-1
		  vector<int> e[N];
		  void dfs(int u){
		  	f[u][1]=w[u];
		  	siz[u]=1;
		  	for(int v:e[u]){
		  		dfs(v);
		  		siz[u]+=siz[v];
		  		for(int j=min(m+1,siz[u]);j>=1;j--)
		  			for(int k=1;k<=min(j-1,siz[v]);k++)
		  				f[u][j]=max(f[u][j],f[u][j-k]+f[v][k]);
		  	}
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n>>m;
		  	for(int i=1,k;i<=n;i++){
		  		cin>>k>>w[i];
		  		e[k].push_back(i);
		  	}
		  	dfs(0);
		  	cout<<f[0][m+1];
		  	return 0;
		  }
		  ```
- 树的重心
- 树的直径
-