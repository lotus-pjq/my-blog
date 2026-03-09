---
title: LCA
date: 2026-03-09
category: 图论
tags:
  - 算法/LCA
  - 算法/图论
  - 技巧/倍增
  - 数据结构/ST表
  - 模板
description: LCA相关的算法笔记和代码模板
---

tags:: #算法/LCA #算法/图论 #技巧/倍增 #数据结构/ST表 #模板

- ## 倍增法（ST表）求LCA
	- 
	- 
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=5e5+5;
	  int n,m,root,dep[N],st[N][20];
	  vector<int> e[N];
	  void dfs(int u,int fa){
	  	dep[u]=dep[fa]+1;
	  	st[u][0]=fa;
	  	for(int i=1;i<=19;i++)
	  		st[u][i]=st[st[u][i-1]][i-1];
	  	for(int v:e[u])
	  		if(v!=fa) dfs(v,u);
	  }
	  int query(int a,int b){
	  	if(dep[a]<dep[b]) swap(a,b);
	  	for(int i=19;i>=0;i--)
	  		if(dep[st[a][i]]>=dep[b])
	      		a=st[a][i];	
	  	if(a==b) return a;
	  	for(int i=19;i>=0;i--)
	    		if(st[a][i]!=st[b][i])
	      		a=st[a][i],b=st[b][i];
	  	return st[a][0];
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	cin>>n>>m>>root;
	  	int u,v;
	  	for(int i=1;i<n;i++){
	  		cin>>u>>v;
	  		e[u].push_back(v);
	  		e[v].push_back(u);
	  	}
	  	dfs(root,0);
	  	for(int i=1;i<=m;i++){
	  		cin>>u>>v;
	  		cout<<query(u,v)<<endl;
	  	}
	  }
	  ```
- ## Tarjan求LCA
	-