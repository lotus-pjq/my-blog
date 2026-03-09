---
title: Educational Codeforces Round 163 (Rated for Div. 2)
date: 2026-03-09
category: 题解
tags:
  - 算法
description: Educational Codeforces Round 163 (Rated for Div. 2)相关的算法笔记和代码模板
---

## B #贪心 #模拟
	- 题意
		- 
		- 
	- 思路
		- 
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  const int N=2e5+5;
		  int a[N];
		  void solve(){
		  	int n;cin>>n;
		  	rep(i,1,n) cin>>a[i];
		  	vector<int> b;b.push_back(a[n]);
		  	for(int i=n-1;i>=1;i--){
		  		if(a[i]>b.back()){
		  			b.push_back(a[i]%10);
		  			b.push_back(a[i]/10);
		  		}else b.push_back(a[i]);
		  	}
		  	cout<<(is_sorted(b.rbegin(),b.rend())?"YES":"NO")<<endl;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;cin>>t;
		      while(t--) solve();
		      return 0;
		  }
		  ```
	- ## D #字符串 #双指针
		- 题目
			- 
			- 
		- 代码
			- ```C++
			  #include<bits/stdc++.h>
			  using namespace std;
			  #define int long long
			  #define endl '\n'
			  #define rep(i,j,k) for (int i=j;i<=k;++i)
			  const int N=2e5+5;
			  void solve(){
			  	int ans=0;
			  	string s;cin>>s;
			  	int n=s.size();
			  	s=' '+s;
			  	rep(d,1,n/2+1){
			  		int cur=0;
			  		for(int l=1;l+d<=n;l++){
			  			if(s[l]==s[l+d]||s[l]=='?'||s[l+d]=='?') cur++;
			  			else cur=0;
			  			if(cur==d) ans=2*cur;
			  		}
			  	}
			  	cout<<ans<<endl;
			  }
			  signed main(){
			      ios::sync_with_stdio(false);
			      cin.tie(nullptr);
			      int t=1;cin>>t;
			      while(t--) solve();
			      return 0;
			  }
			  ```