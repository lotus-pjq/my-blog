---
title: ACM26寒假复习
date: 2026-01-26
category: 数据结构
tags:
  - 算法
outline: deep
---

## 树状数组
- P3374 【模板】树状数组 1

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=5e5+5;
		  int a[N],s[N];
		  int n,m;
		  int lowbit(int x){return x&(-x);}
		  void change(int x,int k){//点修
		  	while(x>n>>m;
		  	for(int i=1,x;i>x;
		  		change(i,x);
		  	}
		  	for(int i=1;i>op>>x>>y;
		  		if(op==1) change(x,y);
		  		else cout
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
		  	while(x>n>>m;
		  	for(int i=1;i>a[i];
		  	for(int i=1,op,x,y,k;i>op;
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