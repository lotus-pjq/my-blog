---
title: Pollard-rho大数质因数分解
date: 2025-10-07
category: 数论
tags:
  - 算法
outline: deep
---

### 预期时间复杂度：O($n^{1/4}$)
- 优化后

```C++
	  #include
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
	          for(int l=1;l1) return d;
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
	      fact(d,fac);
	      fact(x/d,fac);
	  }
	  vectordiv(int n){
	      vectorfac;
	      if(nsav[1001];
	  int a[1001];
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      int n;cin>>n;
	      for(int i=1;i>a[i];
	          sav[i]=div(a[i]);
	      }
	      for(int i=1;i
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
	      if(n>=1,s++;}
	      for(int i=0;i&fac){
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
	      vectorfac;
	      div(n,fac);
	      sort(fac.begin(),fac.end());
	      // coutcnt;
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