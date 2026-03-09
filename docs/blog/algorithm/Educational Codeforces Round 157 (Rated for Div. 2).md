---
title: Educational Codeforces Round 157 (Rated for Div. 2)
date: 2025-10-19
category: 题解
tags:
  - 算法
outline: deep
---

## B #字符串- 题目
  - 
- 分析（代码注释）
- 代码
  - ```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i>n;
		  	int ans=0;
		  	memset(cnt,0,sizeof(cnt));
		  	rep(i,1,n) cin>>s[i];
		  	rep(i,1,n){//预处理cnt[][]
		  		int sum=0;
		  		for(char c:s[i]) sum+=c-'0';
		  		cnt[s[i].size()][sum]++;
		  	}
		  	//左边的字符串比较长
		  	rep(i,1,n){
		  		int l=s[i].size();
		  		// 枚举右边字符串的长度，步长为2（保证总长度为偶数）
		  		for(int r=l%2;r>1;
		  			int hsum=0,rsum=0;
		  			// 计算L的前半部分和
		  			for(int j=0;j=rsum) ans+=cnt[r][hsum-rsum];
		  		}
		  	}
		  	//右边的字符串比较长
		  	rep(i,1,n){
		  		int r=s[i].size();
		  		for(int l=r%2;l>1;
		  			int bsum=0,fsum=0;
		  			for(int j=r-half;j=fsum) ans+=cnt[l][bsum-fsum];
		  		}
		  	}
		  	cout
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  int a[N];
		  int t[N*31][2],idx;
		  void insert(int x){
		  	int p=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(!t[p][j]) t[p][j]=++idx;
		  		p=t[p][j];
		  	}
		  }
		  int query(int x){
		  	int p=0,res=0;
		  	for(int i=30;i>=0;i--){
		  		int j=x>>i&1;
		  		if(t[p][j^1]){
		  			res+=1>n;
		  	for(int i=1;i>a[i];
		  		a[i]^=a[i-1];
		  		insert(a[i]);
		  	}
		  	int num;
		  	for(num=0;num<=n-1;num++)
		  		if(query(num)<n) break;
		  	for(int i=0;i<n;i++) cout<<(a[i]^num)<<' ';
		      return 0;
		  }
		  ```