---
title: 1100F - Ivan and Burgers
date: 2025-08-18
category: 其他
tags:
  - 算法
outline: deep
---

- #前缀线性基
- 
- 
- 
- # 思路：
- 这是一道**前缀**线性基的板子题
- 我们的前缀线性基需要两个变量：*p*[*i*]表示第*i*位的值，*p**os*[*i*]表示对第*i*位造成影响的数的编号。那么很显然，假如我们已经求出了1→*r*的线性基，其中所有*p**os*≥*l*的数构成的线性基就是区间[*l*,*r*]的数构成的线性基
- 根据**贪心**的思想，我们知道，我们要尽可能地让*p**os*[*i*]的值最大，这样才能保证我们通过上述方法构造出的线性基是[*l*,*r*]的线性基
- ==那么如何保证*p**os*[*i*]的值最大呢？==
- 很简单，如果我们插入一个值*x*，它的位置为*w*，那么如果有一位的*p**os*
  using namespace std;
  #define int long long
  #define endl '\n'
  const int N=5e5+5;
  int n,m,x,l,r;
  int p[N][31];   //p[id][i]表示前id个数，第i位的线性基
  int pos[N][31]; //pos[id][i]表示构造基p[id][i]的元素的下标最大值
  void insert(int x,int id){
  	for(int i=0;i=0;i--){
  		if(x>>i&1){
  			//不存在则加入
  			//存在且id更大则交换
  			if(pos[id][i]=0;i--)
  		if(pos[r][i]>=l) ans=max(ans,ans^p[r][i]);
  	return ans;
  }
  signed main(){
  	ios::sync_with_stdio(false);
  	cin.tie(nullptr);
  	cin>>n;
  	for(int i=1;i>x,insert(x,i);
  	cin>>m;
  	while(m--){
  		cin>>l>>r;
  		cout<<query(l,r)<<endl;
  	}
  	return 0;
  }
  ```