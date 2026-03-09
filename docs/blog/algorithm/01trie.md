---
title: 01trie
date: 2026-03-09
category: 数据结构
tags:
  - 算法
outline: deep
---

## 知识点- 
- 
- ## 最大异或对【模板】- 题目- 
- 代码

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  int n,a[N];
		  int t[N*31][2],cnt;
		  void insert(int x){
		  	int p=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(!t[p][j]) t[p][j]=++cnt;
		  		p=t[p][j];
		  	}
		  }
		  int query(int x){
		  	int p=0,res=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(t[p][j^1]){
		  			res+=1>n;
		  	for(int i=1;i>a[i],insert(a[i]);
		  	int ans=0;
		  	for(int i=1;i
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  int a[N];
		  int t[N*31][2],idx;
		  void insert(int x){
		  	int p=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(!t[p][j]) t[p][j]=++idx;
		  		p=t[p][j];
		  	}
		  }
		  int query(int x){
		  	int p=0,res=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(t[p][j^1]){
		  			res+=1>n;
		  	for(int i=1;i>a[i];
		  		a[i]^=a[i-1];
		  		insert(a[i]);
		  	}
		  	int num;
		  	for(num=0;num
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  struct edge{int u,v,w;};
		  vector e[N];
		  int n,pre[N];
		  int t[N*31][2],idx;
		  void insert(int x){
		  	int p=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(!t[p][j]) t[p][j]=++idx;
		  		p=t[p][j];
		  	}
		  }
		  int query(int x){
		  	int p=0,res=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(t[p][j^1]){
		  			res+=1>n;
		  	for(int i=1,u,v,w;i>u>>v>>w;
		  		e[u].push_back({u,v,w});
		  		e[v].push_back({v,u,w});
		  	}
		  	dfs(1,0);
		  	for(int i=1;i<=n;i++) insert(pre[i]);
		  	int mx=0;
		  	for(int i=1;i<=n;i++) mx=max(mx,query(pre[i]));
		  	cout<<mx;
		      return 0;
		  }
		  
		  ```