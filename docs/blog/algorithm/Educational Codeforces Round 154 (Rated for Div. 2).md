---
title: Educational Codeforces Round 154 (Rated for Div. 2)
date: 2026-03-09
category: 题解
tags:
  - 算法
description: Educational Codeforces Round 154 (Rated for Div. 2)相关的算法笔记和代码模板
---

## B #构造
	- 题目
		- 
	- 思路：
		- > 考虑到分成两段
		  然后不要想着把一个变成另一个,把他们俩都变成同一个比如说000000111111
		  抓住这个开头是0结尾是1来构造
		  那就是找是否有相同位置的01就可以了
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define endl '\n'
		  void solve(){
		  	string a,b;cin>>a>>b;
		  	int n=a.size();a=' '+a;b=' '+b;
		  	bool f=0;
		  	for(int i=1;i<n;i++)
		  		if(a[i]=='0'&&a[i+1]=='1'&&b[i]=='0'&&b[i+1]=='1')
		  			f=1;
		  	if(f) cout<<"YES"<<endl;
		  	else cout<<"NO"<<endl;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;cin>>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```
- ## C #模拟
	- 题目
		- 
	- 思路1代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int INF=1e18;
		  void solve(){
		  	int l=1,r=INF,p=0;
		  	string s;cin>>s;
		  	for(int i=0;i<s.size();i++){
		  		if(s[i]=='+') p++;
		  		else if(s[i]=='1'){
		  			if(r!=INF){cout<<"NO"<<endl;return;}
		  			l=p;
		  		}else if(s[i]=='0'){
		  			if(p<=1||l>=p){cout<<"NO"<<endl;return;}
		  			r=min(r,p);
		  		}else{
		  			l=min(--p,l);
		  			if(p<r) r=INF;
		  		}
		  	}
		  	cout<<"YES"<<endl;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;cin>>t;
		      while(t--)solve();
		      return 0;
		  }
		  
		  ```
	- 思路2
- ## D #DP
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
		  int n,a[N];
		  int dp[N][2];
		  /*if(a[i]>a[i-1]){
		  	dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
		  	dp[i][0]=dp[i-1][0]+1;
		  }else if(a[i]<a[i-1]){
		  	dp[i][1]=min(dp[i-1][1],dp[i-1][0])+1;
		  	dp[i][0]=dp[i-1][0];
		  }else{
		  	dp[i][0]=dp[i-1][0]+1;
		  	dp[i][1]=min(dp[i-1][1],dp[i-1][0])+1;
		  }*/
		  //ans=min(dp[n][0]+1,dp[n][1]);
		  void solve(){
		  	cin>>n;
		  	rep(i,1,n) cin>>a[i];
		  	rep(i,2,n){
		  		if(a[i]>a[i-1]){
		  			dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
		  			dp[i][0]=dp[i-1][0]+1;
		  		}else if(a[i]<a[i-1]){
		  			dp[i][1]=min(dp[i-1][1],dp[i-1][0])+1;
		  			dp[i][0]=dp[i-1][0];
		  		}else{
		  			dp[i][0]=dp[i-1][0]+1;
		  			dp[i][1]=min(dp[i-1][1],dp[i-1][0])+1;
		  		}
		  		//cout<<i<<" "<<dp[i][0]<<" "<<dp[i][1]<<endl;
		  	}
		  	cout<<min(dp[n][0]+1,dp[n][1])<<endl;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		      int t=1;cin>>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```