---
title: ACM26寒假复习
date: 2026-03-09
category: 数据结构
tags:
  - 算法
description: ACM26寒假复习相关的算法笔记和代码模板
---

## 树状数组
	- P3374 【模板】树状数组 1
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=5e5+5;
		  int a[N],s[N];
		  int n,m;
		  int lowbit(int x){return x&(-x);}
		  void change(int x,int k){//点修
		  	while(x<=n) s[x]+=k,x+=lowbit(x);
		  }
		  int query(int x){//区查
		  	int sum=0;
		  	while(x) sum+=s[x],x-=lowbit(x);
		  	return sum;
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(0);
		  	cin>>n>>m;
		  	for(int i=1,x;i<=n;i++){
		  		cin>>x;
		  		change(i,x);
		  	}
		  	for(int i=1;i<=m;i++){
		  		int op,x,y;cin>>op>>x>>y;
		  		if(op==1) change(x,y);
		  		else cout<<query(y)-query(x-1)<<endl;
		  	}
		  }
		  ```
	- P3368 【模板】树状数组 2
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  int n,m;
		  int s[N],a[N];
		  int lowbit(int x){return x&(-x);}
		  int query(int x){
		  	int sum=0;
		  	while(x){sum+=s[x];x-=lowbit(x);}
		  	return sum;
		  }
		  void change(int x,int k){
		  	while(x<=n){s[x]+=k;x+=lowbit(x);}
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		  	cin>>n>>m;
		  	for(int i=1;i<=n;i++) cin>>a[i];
		  	for(int i=1,op,x,y,k;i<=m;i++){
		  		cin>>op;
		  		if(op==1){
		  			cin>>x>>y>>k;
		  			change(x,k);change(y+1,-k);
		  		}else if(op==2){
		  			cin>>x;
		  			cout<<a[x]+query(x)<<endl;
		  		}
		  	}
		      return 0;
		  }
		  ```
	- 区修区查--P3372线段树1
		- ```C++
		  ```