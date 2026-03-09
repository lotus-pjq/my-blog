---
title: 2024武汉ICPC邀请赛-G
date: 2025-10-10
category: 题解
tags:
  - 算法
outline: deep
---

- 题目
- 
	-
- 思路
- 
- 
- 答案
- ```C++
	  #include
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=2e5+5;
	  int ans;
	  int exgcd(int a,int b,int &x,int &y){//a*x+b*y=gcd
	  	if(b==0){x=1,y=0;return a;}
	  	int d=exgcd(b,a%b,y,x);
	  	y-=a/b*x;
	  	return d;
	  }
	  void cal(int n,int m,int x,int y,int dx,int dy){
	  	for(int l=1,r;l=tl){
	  			if(dx>=dy) ans=min(ans, n+m-(x+y+tr*(dx-dy))*p );
	  			else ans=min(ans, n+m-(x+y+tl*(dx-dy))*p );
	  		}
	  	}
	  }
	  void solve(){
	  	int n,m,a,b,k;cin>>n>>m>>a>>b>>k;
	  	ans=n+m;
	  	int x,y;
	  	int g=exgcd(a,b,x,y);
	  	//a*x+b*y=k
	  	x*=k/g;
	  	y*=k/g;
	  	int dx=b/g;
	  	int dy=a/g;
	  	int Xmin,Ymax,Xmax,Ymin;
	  	//取(x,y)=(Xmin,Ymax)
	  	Xmin=(x%dx+dx)%dx;
	  	Ymax=(k-a*Xmin)/b;
	  	Ymin=(y%dy+dy)%dy;
	  	Xmax=(k-b*Ymin)/a;
	  	if(k%g!=0){cout>t;
	      while(t--) solve();
	      return 0;
	  }
	  
	  ```