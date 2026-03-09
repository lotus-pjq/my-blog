---
title: Pollard-rho大数质因数分解
date: 2026-03-09
category: 数论
tags:
  - 算法
description: Pollard-rho大数质因数分解相关的算法笔记和代码模板
---

### 预期时间复杂度：O($n^{1/4}$)
- 优化后
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
	                  if(d>1) return d;
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
	      fact(d,fac);
	      fact(x/d,fac);
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
	  int a[1001];
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      int n;cin>>n;
	      for(int i=1;i<=n;i++){
	          cin>>a[i];
	          sav[i]=div(a[i]);
	      }
	      for(int i=1;i<=n;i++){
	          for(int num:sav[i])cout<<num<<" ";
	          cout<<endl;
	      }
	      return 0;
	  }
	  ```
- 优化前
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  mt19937_64 rg(random_device{}());
	  int ksm(int a,int b,int mod) {
	      int res=1;a%=mod;
	      while(b){
	          if(b&1) res=(__int128)res*a%mod;
	          a=(__int128)a*a%mod;
	          b>>=1;
	      }return res;
	  }
	  bool is_prime(int n){
	      if(n<2) return false;
	      if(n==2) return true;
	      if(n%2==0) return false;
	      int a[]={2,325,9375,28178,450775,9780504,1795265022};
	      int d=n-1;
	      int s=0;
	      while(d%2==0){d>>=1,s++;}
	      for(int i=0;i<7&&a[i]<n;i++){
	          int x=ksm(a[i],d,n);
	          if(x==1||x==n-1) continue;
	          bool flag=true;
	          for(int j=0;j<s-1;j++){
	              x=(__int128)x*x%n;
	              if(x==n-1){flag=false;break;}
	          }
	          if(flag) return false;
	      }
	      return true;
	  }
	  int pollard_rho(int n){
	      if(n==1) return n;
	      if(n%2==0)return 2;
	      int x=(rg()%(n-2))+2;
	      int y=x;
	      int c=(rg()%(n-1))+1;
	      int d=1;
	      auto f=[&](int x){return ((__int128)x*x+c)%n;};
	      while(d==1){
	          x=f(x);
	          y=f(f(y));
	          d=__gcd(abs(x-y),n);
	          if(d==n){
	              x=(rg()%(n-2))+2;
	              y=x;
	              c=(rg()%(n-1))+1;
	              d=1;
	          }
	      }
	      return d;
	  }
	  void div(int n,vector<int>&fac){
	      if(n==1) return;
	      if(is_prime(n)){fac.push_back(n);return;}
	      int d=pollard_rho(n);
	      div(d,fac);
	      div(n/d,fac);
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	      int n;cin>>n;//n>=2
	      vector<int>fac;
	      div(n,fac);
	      sort(fac.begin(),fac.end());
	      // cout<<n<<" = ";
	      // map<int,int>cnt;
	      // for(int fact:fac) cnt[fact]++;
	      // bool first=true;
	      // for(auto&[fact,cnt]:cnt){
	      //     if(!first)cout<<" * ";
	      //     first=false;
	      //     if(cnt==1) cout<<fact;
	      //     else cout<<fact<<"^"<<cnt;
	      // }
	      // cout<<endl;
	      return 0;
	  }
	  ```