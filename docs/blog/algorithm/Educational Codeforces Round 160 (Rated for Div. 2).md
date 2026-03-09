---
title: Educational Codeforces Round 160 (Rated for Div. 2)
date: 2026-03-09
category: 题解
tags:
  - 算法
description: Educational Codeforces Round 160 (Rated for Div. 2)相关的算法笔记和代码模板
---

## B
	- 题目
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
		  int pre1[N],pre0[N];
		  void solve(){
		  	string s;cin>>s;
		  	int n=s.size();
		  	s=' '+s;
		  	for(int i=1;i<=n;i++){
		  		pre1[i]=pre1[i-1];
		  		pre0[i]=pre0[i-1];
		  		if(s[i]=='0') pre0[i]++;
		  		else pre1[i]++;
		  	}
		  	int cnt0=pre0[n],cnt1=pre1[n];
		  	int pos=0;
		  	while(pos<n&&pre0[pos+1]<=cnt1&&pre1[pos+1]<=cnt0) pos++;
		  	cout<<n-pos<<endl;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;cin>>t;
		      while(t--) solve();
		      return 0;
		  }
		  ```
- ## Ｃ #按位 #贪心 #1300
	- 题目
		- 
		- 
	- 思路
		- 如果没有二进制的话就是背包。
		- 但有了二进制的组合后就可以贪心的取了
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  const int N=2e5+5;
		  int cnt[32];
		  void solve(){
		  	int n,op,x;cin>>n;
		  	memset(cnt,0,sizeof(cnt));
		  	rep(i,1,n){
		  		cin>>op>>x;
		  		if(op==1){cnt[x]++;}
		  		else{
		  			for(int i=30;i>=0;i--){
		  				int tmp=x/(1<<i);
		  				x-=min(tmp,cnt[i])*(1<<i);
		  			}
		  			if(x==0) cout<<"YES"<<endl;
		  			else cout<<"NO"<<endl;
		  		}
		  	}
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;
		      while(t--) solve();
		      return 0;
		  }
		  ```
- ## D #笛卡尔树 #分治 #栈 #DP #2100
	- 题目
		- 
		- 
		-
	- 思路1（笛卡尔树）
		- 1.区间[ l , r ] = ans[ l , p-1 ] * ans[ p+1 , r ];
		- 2.如果在 [ 1 , l-1 ] 的部分有比最小元素更小的数字 ans[ l , r ] += ans[ p+1 , r ];
		- 3.如果在 [ r+1 , n ]的部分有比最小元素更小的数字 ans[ l , r ] += ans[ l , p-1 ];
		- 4.如果左边和右边都有比最小元素更小的数字 ans[ l , r ]--;
	- 代码1（笛卡尔树）
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  const int N=3e5+5;
		  const int mod=998244353;
		  int n,a[N],root;
		  int ls[N],rs[N],sta[N];
		  void build(){
		  	int top=0;
		  	for(int i=1;i<=n;i++){
		  		int pos=top;
		  		while(pos>0&&a[sta[pos]]>a[i]) pos--;
		  		if(pos>0) rs[sta[pos]]=i;
		  		if(pos<top) ls[i]=sta[pos+1];
		  		sta[++pos]=i;
		  		top=pos;
		  	}
		  	root=sta[1];
		  }
		  int dfs(int l,int r,int x,int fa){
		  	if(l>r) return 1;
		  	int ansl=dfs(l,x-1,ls[x],x);
		  	int ansr=dfs(x+1,r,rs[x],x);
		  	int res=ansl*ansr%mod;
		  	if(l>1) res+=ansr;
		  	if(r<n) res+=ansl;
		  	if(l>1&&r<n) res=(res+mod-1)%mod;
		  	return res%mod;
		  }
		  void solve(){
		  	cin>>n;
		  	rep(i,1,n) cin>>a[i];
		  	build();
		  	cout<<dfs(1,n,root,0)<<endl;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;cin>>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```
-