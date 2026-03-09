---
title: G.移除质数(2020-2021 Winter Petrozavodsk Camp, Day 5)
date: 2026-03-09
category: 数论
tags:
  - 算法
description: G.移除质数(2020-2021 Winter Petrozavodsk Camp, Day 5)相关的算法笔记和代码模板
---

- 网站[Problem - G - Codeforces](https://codeforces.com/gym/103260/problem/G)
- 题目
	- 
- 题意描述
	- 给一个长度为$$n$$的数列$$a$$，两个人玩游戏，每次必须选择一个质数$$p$$和一个区间$$[l,r]$$，要求$$[l,r]$$中每个数都包含质因子$$p$$，然后把它们所有因子$$p$$去掉，无法操作者输，求哪方获胜。其中$$n<=1000 , a_i<=10^{18}$$
- 思路
	- 考虑用SG函数，则每个质数是独立的，可以分开考虑再把SG值异或起来。
	- 对于每个质数$$p$$，根据$$a_i$$是否含有$$p$$的因子可以把它们分成两类，实际上又分成了若干个子游戏。打表可以发现，对于连续$$i$$个数，它们的SG值就是$$i$$。
	- 后面就是利用pollard-rho对大数进行质因数分解。
- SG函数部分打表
	- 结论：$$sg(i)=i$$
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=2e5+5;
	  int sg[N];
	  int SG(int x){
	  	if(sg[x]!=-1) return sg[x];
	  	set<int> st;
	  	for(int sta=1;sta<=x;sta++)
	  		for(int len=1;len<=x-sta+1;len++)
	  			st.insert(SG(sta-1)^SG(x+1-(sta+len)));
	  	int p=0;
	  	while(st.count(p)) p++;
	  	return sg[x]=p;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	memset(sg,-1,sizeof(sg));
	  	sg[0]=0,sg[1]=1;
	  	int n;cin>>n;
	  	for(int i=1;i<=n;i++) cout<<i<<":"<<SG(i)<<endl;
	  	return 0;
	  }
	  ```
- 代码
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  mt19937_64 rg(random_device{}());
	  int gcd(int a,int b){
	      int tmp;
	      while(b!=0){tmp=a%b;a=b;b=tmp;}
	      return a;
	  }
	  int ksm(int x,int p,int mod){
	      int res=1;
	      while(p){
	          if(p&1ll)res=(__int128)res*x%mod;
	          x=(__int128)x*x%mod;p>>=1;
	      }return res;
	  }
	  const int ds[7]={2,325,9375,28178,450775,9780504,1795265022};
	  bool is_prime(int n){
	      if(n<3||!(n&1ll)) return n==2;
	      int u=n-1,t=0;
	      while(!(u&1ll))t++,u>>=1;
	      for(int k:ds){
	          int v=ksm(k,u,n);
	          if(v==1||v==n-1||v==0) continue;
	          for(int l=1;l<=t;l++){
	              v=(__int128)v*v%n;
	              if(v==n-1&&l<t){v=1;break;}
	              if(v==1) return false;
	          }
	          if(v!=1) return false;
	      }
	      return true;
	  }
	  int pollard_rho(int x){
	      int s=0,t=0;
	      int c=(int)rg()%(x-1)+1;
	      for(int goal=1,val=1;;goal*=2,s=t,val=1){
	          for(int step=1;step<=goal;step++){
	              t=((__int128)t*t+c)%x;
	              val=(__int128)val*abs(t-s)%x;
	              if((step%127)==0){
	                  int d=gcd(val,x);
	                  if(d>1)return d;
	              }
	          }
	          int d=gcd(val,x);
	          if(d>1)return d;
	      }
	  }
	  void fact(int x,vector<int>&fac){//递归
	      if(x==1) return;
	      if(is_prime(x)){fac.push_back(x);return;}
	      int d=pollard_rho(x);
	  	int res=x;
	  	while(res%d==0) res/=d;
	      fact(d,fac);
	      fact(res,fac);
	  }
	  vector<int>div(int n){
	      vector<int>fac;
	      if(n<=1) return fac;
	      fact(n,fac);
	      sort(fac.begin(),fac.end());
	      fac.erase(unique(fac.begin(),fac.end()),fac.end());//去重
	      return fac;
	  }
	  vector<int>sav[1001];
	  map<int,vector<int>> mp;
	  int a[1001];
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      int n;cin>>n;
	      for(int i=1;i<=n;i++){
	          cin>>a[i];
	          sav[i]=div(a[i]);
	      }
	  	for(int i=1;i<=n;i++)
	  		for(int x:sav[i])
	  			mp[x].push_back(i);
	  	int res=0;
	  	for(auto pr:mp){
	  		int x=pr.first;
	  		vector<int> pos=pr.second;
	  		int cur=0,last=pos[0],cnt=1;
	  		for(int i=1;i<pos.size();i++){
	  			if(pos[i]!=last+1){
	  				cur^=cnt;
	  				cnt=1;
	  			}else cnt++;
	  			last=pos[i];
	  		}
	  		cur^=cnt;
	  		res^=cur;
	  	}
	  	if(res) cout<<"First"<<endl;
	  	else cout<<"Second"<<endl;
	      return 0;
	  }
	  ```