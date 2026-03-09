---
title: 最长上升子序列(LIS)
date: 2026-03-09
category: 动态规划
tags:
  - 算法
description: 最长上升子序列(LIS)相关的算法笔记和代码模板
---

## 分析：
	- 
- ## Code：
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=1e6+5;
	  int a[N],b[N],len,n;
	  int find(int x){
	  	int l=1,r=len,mid;
	  	while(l<=r){
	  		mid=l+r>>1;
	  		if(b[mid]>=x) r=mid-1;
	  		else l=mid+1;
	  	}
	  	return l;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	cin>>n;
	  	for(int i=1;i<=n;i++) cin>>a[i];
	  	for(int i=1;i<=n;i++){
	  		if(a[i]>b[len]) b[++len]=a[i];
	  		else b[find(a[i])]=a[i];
	  	}
	  	cout<<len;
	  	return 0;
	  }
	  ```
-