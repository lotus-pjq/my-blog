---
title: Educational Codeforces Round 163 (Rated for Div. 2)
date: 2025-10-16
category: 题解
tags:
  - 算法
outline: deep
---

## B #贪心 #模拟
- 题意- 
  - 
- 思路- 
- 代码

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i>n;
		  	rep(i,1,n) cin>>a[i];
		  	vector b;b.push_back(a[n]);
		  	for(int i=n-1;i>=1;i--){
		  		if(a[i]>b.back()){
		  			b.push_back(a[i]%10);
		  			b.push_back(a[i]/10);
		  		}else b.push_back(a[i]);
		  	}
		  	cout>t;
		      while(t--) solve();
		      return 0;
		  }
		  ```
- ## D #字符串 #双指针
  - 题目- 
  - 
  - 代码
  - ```C++
			  #include
			  using namespace std;
			  #define int long long
			  #define endl '\n'
			  #define rep(i,j,k) for (int i=j;i>s;
			  	int n=s.size();
			  	s=' '+s;
			  	rep(d,1,n/2+1){
			  		int cur=0;
			  		for(int l=1;l+d>t;
			      while(t--) solve();
			      return 0;
			  }
			  ```