---
title: 2018ICPC南京区域赛-G
date: 2026-03-09
category: 题解
tags:
  - 算法
description: 2018ICPC南京区域赛-G相关的算法笔记和代码模板
---

- 题目
	- 
	- 
- 思路
	- 和25CCPC网络赛的A题，那道矩形网格每个点作为顶点的正方形计数的原理几乎一模一样。
	- 框定大小后能贡献多少个刚刚好卡在里面的。
	- 具体算式就不写了。
	- 结论是C(n+3,4)
- 代码
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int mod=1e9+7;
	  int ksm(int a,int b,int c=mod){
	  	int ans=1;
	  	while(b){
	  	   if(b&1) ans=(ans*a)%c;
	  	   b>>=1,a=(a*a)%c;
	  	}return ans;
	  }
	  const int inv24=ksm(24,mod-2);
	  void mul(int &x,int y){x=x*y%mod;}
	  void solve(){
	  	int n;cin>>n;
	  	int ans=1;
	  	mul(ans,n+3);
	  	mul(ans,n+2);
	  	mul(ans,n+1);
	  	mul(ans,n);
	  	mul(ans,inv24);
	  	cout<<ans<<endl;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	int t;cin>>t;
	  	while(t--) solve();
	  	return 0;
	  }
	  ```