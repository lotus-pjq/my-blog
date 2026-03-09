---
title: Educational Codeforces Round 152 (Rated for Div. 2)
date: 2026-03-09
category: 题解
tags:
  - 算法
description: Educational Codeforces Round 152 (Rated for Div. 2)相关的算法笔记和代码模板
---

## D #贪心
	- 题目：
		- 
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  const int N=2e5+5;
		  int n,a[N],ans;
		  bool vis[N];
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n;
		  	rep(i,1,n) cin>>a[i];
		  	for(int i=1;i<=n;i++){
		  		if(a[i]==2&&!vis[i]){
		  			ans++;
		  			int l=i;
		  			while(a[l]) vis[l]=1,l--;
		  			vis[l]=1;
		  			int r=i;
		  			while(a[r]) vis[r]=1,r++;
		  			vis[r]=1;
		  		}
		  	}
		  	for(int i=1;i<=n;i++){
		  		if(a[i]==1&&!vis[i]){
		  			ans++;
		  			bool used=1;
		  			if(!vis[i-1]&&i>1) vis[i-1]=1,used=0;
		  			int l=i;
		  			while(a[l]) vis[l]=1,l++;
		  			if(used) vis[l]=1;
		  		}
		  	}
		  	for(int i=1;i<=n;i++)
		  		if(!vis[i]) ans++;
		  	cout<<ans;
		  	return 0;
		  }
		  ```