---
title: G.移除质数(2020-2021 Winter Petrozavodsk Camp, Day 5)
date: 2025-10-23
category: 博弈论
tags:
  - 算法
outline: deep
---

- 网站[Problem - G - Codeforces](https://codeforces.com/gym/103260/problem/G)
- 题目- 
- 题意描述
- 给一个长度为$$n$$的数列$$a$$，两个人玩游戏，每次必须选择一个质数$$p$$和一个区间$$[l,r]$$，要求$$[l,r]$$中每个数都包含质因子$$p$$，然后把它们所有因子$$p$$去掉，无法操作者输，求哪方获胜。其中$$n
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=2e5+5;
	  int sg[N];
	  int SG(int x){
	  	if(sg[x]!=-1) return sg[x];
	  	set st;
	  	for(int sta=1;sta>n;
	  	for(int i=1;i
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
	      if(n>=1;
	      for(int k:ds){
	          int v=ksm(k,u,n);
	          if(v==1||v==n-1||v==0) continue;
	          for(int l=1;l1)return d;
	              }
	          }
	          int d=gcd(val,x);
	          if(d>1)return d;
	      }
	  }
	  void fact(int x,vector&fac){//递归
	      if(x==1) return;
	      if(is_prime(x)){fac.push_back(x);return;}
	      int d=pollard_rho(x);
	  	int res=x;
	  	while(res%d==0) res/=d;
	      fact(d,fac);
	      fact(res,fac);
	  }
	  vectordiv(int n){
	      vectorfac;
	      if(nsav[1001];
	  map> mp;
	  int a[1001];
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      int n;cin>>n;
	      for(int i=1;i>a[i];
	          sav[i]=div(a[i]);
	      }
	  	for(int i=1;i pos=pr.second;
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