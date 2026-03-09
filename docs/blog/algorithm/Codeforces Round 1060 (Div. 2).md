---
title: Codeforces Round 1060 (Div. 2)
date: 2025-10-20
category: 数论
tags:
  - 算法
outline: deep
---

## C2 #数学 #筛法 #gcd- 题目- 
  - 
- 分析- 
- 代码

```C++
		  #include
		  using namespace std;
		  #define fi first
		  #define se second
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  struct node{
		  	int a,b;
		  	bool operator mpf;
		  void sieve(int n){
		  	mpf.resize(n+1,0);
		  	for(int i=2;i st;
		  	cin>>n;
		  	for(int i=1;i>x[i].a;
		  	for(int i=1;i>x[i].b;
		  	sort(x+1,x+n+1);
		  	for(int i=1;i tmp;
		  		while(cur>1){
		  			int p=mpf[cur];
		  			if(st.count(p)){cout1){
		  			int p=mpf[cur];
		  			if(st.count(p)){ans=min(ans,x[i].b);break;}
		  			while(cur%p==0) cur/=p;
		  		}
		  	}
		  	int cnt=2e9;//不能太大，不然下面cnt*x[1].b会爆longlong
		  	for(int i=2;i1){
		  			int p=mpf[cur];
		  			cnt=min(cnt,p-x[1].a%p);
		  			while(cur%p==0) cur/=p;
		  		}
		  	}
		  	ans=min(ans,cnt*x[1].b);
		  	cout>t;
		  	while(t--) solve();
		  	return 0;
		  }
		  ```