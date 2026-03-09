---
title: Educational Codeforces Round 158 (Rated for Div. 2)
date: 2025-10-01
category: 题解
tags:
  - 算法
outline: deep
---

## B #trick
- 题目- 
- 代码

```C++
		  #include
		  using namespace std;
		  #define INF 0x3f3f3f3f3f3f3f3f
		  #define rep(i,j,k) for (int i=j;i>n;
		  	rep(i,1,n) cin>>a[i];
		  	int ans=-1;
		  	rep(i,1,n) ans+=max(0ll,a[i]-a[i-1]);
		  	cout>t;
		  	while(t--) solve();
		  	return 0;
		  }
		  ```
- ## C
- 题目- 
- 代码

```C++
		  #include
		  using namespace std;
		  #define INF 0x3f3f3f3f3f3f3f3f
		  #define rep(i,j,k) for (int i=j;i>n;
		  	int mn=INF,mx=0;
		  	rep(i,1,n){
		  		cin>>a[i];
		  		mx=max(mx,a[i]);
		  		mn=min(mn,a[i]);
		  	}
		  	int cnt=0;
		  	while(mn!=mx){
		  		ans[++cnt]=mn;
		  		mx=mx+mn>>1;
		  	}
		  	if(cnt>n) cout>t;
		  	while(t--) solve();
		  	return 0;
		  }
		  ```
- ## D #trick
- 题目- 
  - 
  - 
- 思路- 
  - > ans=min{i=1->n}(max{j=1->(i-1)}(aj+n-j),max{j=i+1->n}(aj+j-1))
		  维护前缀max{aj-j+n}和后缀max{aj+j-1}
- 代码

```C++
		  #include
		  using namespace std;
		  #define INF 0x3f3f3f3f3f3f3f3f
		  #define rep(i,j,k) for (int i=j;i=k;--i)
		  #define int long long
		  #define endl '\n'
		  const int N=3e5+5;
		  int n,m,a[N],pre[N],suf[N];
		  //ans=min{i=1->n}(max{j=1->(i-1)}(aj+n-j),max{j=i+1->n}(aj+j-1))
		  //维护前缀max{aj-j+n}和后缀max{aj+j-1}
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	int n;cin>>n;
		  	rep(i,1,n) cin>>a[i];
		  	rep(i,1,n) pre[i]=a[i]-i+n;
		  	rep(i,1,n) suf[i]=a[i]+i-1; 
		  	rep(i,2,n) pre[i]=max(pre[i-1],pre[i]);
		  	per(i,n-1,1) suf[i]=max(suf[i+1],suf[i]);
		  	int ans=INF,cur;
		  	for(int i=1;i1) cur=max(cur,pre[i-1]);
		  		if(i<n) cur=max(cur,suf[i+1]);
		  		ans=min(ans,cur);
		  	}
		  	cout<<ans;
		  	return 0;
		  }
		  ```
- 