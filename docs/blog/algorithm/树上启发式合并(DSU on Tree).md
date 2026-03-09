---
title: 树上启发式合并(DSU on Tree)
date: 2026-03-09
category: 图论
tags:
  - 算法
description: 树上启发式合并(DSU on Tree)相关的算法笔记和代码模板
---

## 引入(OIwiki) :
	- #### Q:启发式算法是什么呢？
	- #### A:启发式算法是基于人类的经验和直观感觉，对一些算法的优化。
	- 举个例子，最常见的就是**并查集的启发式合并**了，代码是这样的： 
	  ```
	  void merge(int x, int y) {
	    int xx = find(x), yy = find(y);
	    if (size[xx] < size[yy]) swap(xx, yy);
	    fa[yy] = xx;
	    size[xx] += size[yy];
	  }
	  ```
	  
	  在这里，**对于两个大小不一样的集合，我们将小的集合合并到大的集合中，而不是将大的集合合并到小的集合中。**
	  为什么呢？这个集合的大小可以认为是集合的高度（在正常情况下），而我们将集合高度小的并到高度大的显然有助于我们找到父亲。
	  让高度小的树成为高度较大的树的子树，这个优化可以称为启发式合并算法。
- ## 分析：
	- ### 先跑重链剖分，预处理出每个节点的重儿子
	- ### 按照一下步骤遍历每个节点x：
		- #### 1.先遍历x的轻儿子，并计算答案，但不保留遍历后对它cnt数组的贡献
		- #### 2.遍历x的重儿子，保留遍历后它对cnt数组的贡献
		- #### 3.再次遍历x的轻儿子，加入轻子树的贡献，得到x的答案(树上启发式合并：轻子树的结果并入重子树)。
	- 
	- 
	- 
- ## CF600E Lomsat gelral([Educational Codeforces Round 2](https://codeforces.com/contest/600))
	- ## 题目：
		- 
	- ## Code:
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=1e5+10;
		  int n,col[N],siz[N],son[N],cnt[N],mx;
		  int sum,ans[N];
		  vector<int>e[N];
		  void dfs1(int x,int fa){ 
		  	siz[x]=1;
		  	for(int y:e[x]){
		  		if(y==fa) continue;
		  		dfs1(y,x);
		  		siz[x]+=siz[y];
		  		if(siz[y]>siz[son[x]]) son[x]=y;
		  	}
		  }
		  void add(int x,int fa,int son){
		  	cnt[col[x]]++;
		  	if(cnt[col[x]]>mx) mx=cnt[col[x]],sum=col[x];
		  	else if(cnt[col[x]]==mx) sum+=col[x];
		  	for(int y:e[x]) //重子树除外
		  		if(y!=fa&&y!=son) add(y,x,son);
		  }
		  void sub(int x,int fa){//减去轻子树贡献
		  	cnt[col[x]]--;
		  	for(int y:e[x])
		  		if(y!=fa) sub(y,x);
		  }
		  void dfs2(int x,int fa,int opt){
		  	//opt:0->轻儿子,1->重儿子
		  	for(int y:e[x]) //先搜轻儿子，确定轻儿子的ans[x]
		  		if(y!=fa&&y!=son[x]) dfs2(y,x,0);
		  	if(son[x]) dfs2(son[x],x,1); //再搜重儿子
		  	add(x,fa,son[x]); //累计x和轻子树贡献
		  	ans[x]=sum;       
		  	if(!opt) sub(x,fa),sum=mx=0;//减去轻子树贡献并清空
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n;
		  	for(int i=1;i<=n;i++) cin>>col[i];
		  	for(int i=1,x,y;i<n;i++){
		  		cin>>x>>y;
		  		e[x].push_back(y);
		  		e[y].push_back(x);
		  	}
		  	dfs1(1,0);
		  	dfs2(1,0,0);
		  	for(int i=1;i<=n;i++) cout<<ans[i]<<" ";
		  	return 0;
		  }
		  ```
- ## G. Tree problem([ICPC Central Russia Regional Contest, 2024](https://codeforces.com/gym/106035))
	- ## 题目:
		- 
	- ## Code:
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+10;
		  int n,col[N],siz[N],son[N],mx;
		  unordered_map<int,int> cnt;
		  int ans[N],color,root;
		  int indgr[N];
		  vector<int>e[N];
		  void dfs1(int x,int fa){ 
		  	siz[x]=1;
		  	for(int y:e[x]){
		  		if(y==fa) continue;
		  		dfs1(y,x);
		  		siz[x]+=siz[y];
		  		if(siz[y]>siz[son[x]]) son[x]=y;
		  	}
		  }
		  void add(int x,int fa,int son){
		  	cnt[col[x]]++;
		  	if(cnt[col[x]]>mx) mx=cnt[col[x]],color=col[x];
		  	else if(cnt[col[x]]==mx&&color>col[x]) color=col[x];
		  	for(int y:e[x]) //重子树除外
		  		if(y!=fa&&y!=son) add(y,x,son);
		  }
		  void sub(int x,int fa){//减去轻子树贡献
		  	cnt[col[x]]--;
		  	for(int y:e[x])
		  		if(y!=fa) sub(y,x);
		  }
		  void dfs2(int x,int fa,int opt){
		  	//opt:0->轻儿子,1->重儿子
		  	for(int y:e[x]) //先搜轻儿子，确定轻儿子的ans[x]
		  		if(y!=fa&&y!=son[x]) dfs2(y,x,0);
		  	if(son[x]) dfs2(son[x],x,1); //再搜重儿子
		  	add(x,fa,son[x]); //累计x和轻子树贡献
		  	ans[x]=color;       
		  	if(!opt) sub(x,fa),mx=0;//减去轻子树贡献并清空
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n;
		  	for(int i=1;i<=n;i++) cin>>col[i];
		  	for(int i=1,x,y;i<n;i++){
		  		cin>>x>>y;
		  		indgr[y]++;
		  		e[x].push_back(y);
		  		e[y].push_back(x);
		  	}
		  	for(int i=1;i<=n;i++)
		  		if(!indgr[i]){root=i;break;}
		  	dfs1(root,0);
		  	dfs2(root,0,0);
		  	for(int i=1;i<=n;i++) cout<<ans[i]<<" ";
		  	return 0;
		  }
		  ```