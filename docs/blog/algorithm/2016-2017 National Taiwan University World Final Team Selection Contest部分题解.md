---
title: 2016-2017 National Taiwan University World Final Team Selection Contest部分题解
date: 2026-03-09
category: 数据结构
tags:
  - 算法
description: 2016-2017 National Taiwan University World Final Team Selection Contest部分题解相关的算法笔记和代码模板
---

- PDF
	- [national-taiwan-university-world-final-team-selection-contest-en.pdf](https://codeforces.com/gym/101234/attachments/download/5080/national-taiwan-university-world-final-team-selection-contest-en.pdf)
- ## A #二分答案 #线段树
	- 题目(2016-2017 National Taiwan University World Final Team Selection Contest --- A)
		- 
	- 题意描述
		- 给定一个长度为n的序列a, 有m次操作，每次操作选择一个区间[L,R], 将区间内的数从小到大排序，或从大到小排序，问最终序列中间的数是什么。
	- 思路
		- 二分答案mid，将小于mid的数变成−1，大于mid的数变成1，等于mid的数为0，每次操作相当于询问某个区间内−1或1的个数，然后将区间重新染色，这个可以用线段树维护。最终如果中间的数是0，则二分的值就是答案，如果是−1说明答案偏大，否则答案偏小。
		- 时间复杂度: O(n\*logn\*logn)
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  #define ls x<<1
		  #define rs x<<1|1
		  const int N=1e5+5;
		  struct node{
		  	int l,r,lazy;
		  	int neg,zero,pos;
		  }t[N<<2];
		  int n,k,jud;
		  int a[N],ql[N],qr[N];
		  void up(int x){
		  	t[x].neg=t[ls].neg+t[rs].neg;
		  	t[x].zero=t[ls].zero+t[rs].zero;
		  	t[x].pos=t[ls].pos+t[rs].pos;
		  }
		  void down(int x){
		  	if(t[x].lazy!=-2){
		  		if(t[x].lazy==-1){
		  			t[ls].neg=t[ls].r-t[ls].l+1;
		  			t[ls].pos=t[ls].zero=0;
		  			t[rs].neg=t[rs].r-t[rs].l+1;
		  			t[rs].pos=t[rs].zero=0;
		  		}else if(t[x].lazy==0){
		  			t[ls].neg=t[ls].pos=t[rs].neg=t[rs].pos=0;
		  			t[ls].zero=t[rs].zero=1;
		  		}else if(t[x].lazy==1){
		  			t[ls].pos=t[ls].r-t[ls].l+1;
		  			t[rs].pos=t[rs].r-t[rs].l+1;
		  			t[ls].neg=t[ls].zero=t[rs].neg=t[rs].zero=0;
		  		}
		  		t[ls].lazy=t[rs].lazy=t[x].lazy;
		  		t[x].lazy=-2;
		  	}
		  }
		  void build(int x,int l,int r){
		  	t[x]={l,r,-2,0,0,0};
		  	if(l==r){
		  		if(a[l]<jud) t[x].neg=1;
		  		else if(a[l]==jud) t[x].zero=1;
		  		else t[x].pos=1;
		  		return;
		  	}
		  	build(ls,l,l+r>>1),build(rs,(l+r>>1)+1,r);
		  	up(x);
		  }
		  void update(int x,int l,int r,int val){
		  	if(t[x].l>r||t[x].r<l) return;
		  	if(t[x].l>=l&&t[x].r<=r){
		  		t[x].neg=t[x].zero=t[x].pos=0;
		  		if(val==-1) t[x].neg=t[x].r-t[x].l+1;
		  		else if(val==1) t[x].pos=t[x].r-t[x].l+1;
		  		else if(val==0) t[x].zero=1;
		  		t[x].lazy=val;
		  		return;
		  	}
		  	down(x);
		  	update(ls,l,r,val),update(rs,l,r,val);
		  	up(x);
		  }
		  void query(int x,int l,int r,int &neg,int &zero,int &pos){
		  	if(t[x].l>r||t[x].r<l){neg=zero=pos=0;return;}
		  	if(t[x].l>=l&&t[x].r<=r){neg=t[x].neg,zero=t[x].zero,pos=t[x].pos;return;}
		  	down(x);
		  	int n1,z1,p1,n2,z2,p2;
		  	query(ls,l,r,n1,z1,p1);
		  	query(rs,l,r,n2,z2,p2);
		  	neg=n1+n2,zero=z1+z2,pos=p1+p2;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		  	cin>>n>>k;
		  	rep(i,1,n) cin>>a[i];
		  	rep(i,1,k) cin>>ql[i]>>qr[i];
		  	int l=1,r=n,mid,ans;
		  	while(l<=r){
		  		jud=mid=l+r>>1;
		  		build(1,1,n);
		  		int cnt_neg,cnt_zero,cnt_pos;
		  		for(int i=1,l,r;i<=k;i++){
		  			l=ql[i],r=qr[i];
		  			bool u=l<r;
		  			if(!u) swap(l,r);
		  			query(1,l,r,cnt_neg,cnt_zero,cnt_pos);
		  			if(!u){
		  				if(cnt_pos) update(1,l,l+cnt_pos-1,1);
		  				if(cnt_zero) update(1,l+cnt_pos,l+cnt_pos,0);
		  				if(cnt_neg) update(1,r-cnt_neg+1,r,-1);
		  			}else{
		  				if(cnt_neg) update(1,l,l+cnt_neg-1,-1);
		  				if(cnt_zero) update(1,l+cnt_neg,l+cnt_neg,0);
		  				if(cnt_pos) update(1,r-cnt_pos+1,r,1);
		  			}
		  		}
		  		query(1,(n+1)/2,(n+1)/2,cnt_neg,cnt_zero,cnt_pos);
		  		if(cnt_zero){ans=mid;break;}
		  		else if(cnt_neg==1) r=mid-1;
		  		else l=mid+1;
		  	}
		  	cout<<ans;
		      return 0;
		  }
		  ```
- ## G #堆 #思维 #第k小
	- 题意描述
		- 有n个数，找出所有子集中，和为第k小的子集和。
	- 思路1
		- 将食物从小到大排序，用堆记录(代价,最贵的食物)，每次要么新加入一个更贵的食物，要么把最贵的换成更贵的。时间复杂度O(nlogn+klogk)。
	- 代码(思路1）
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  #define pii pair<int,int>
		  int n,m,a[N];
		  priority_queue<pii,vector<pii>,greater<pii>> q;
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n>>m;
		  	for(int i=1;i<=n;i++) cin>>a[i];
		  	sort(a+1,a+n+1);
		  	q.push({a[1],1});
		  	pii t=q.top();
		  	while(m--){
		  		t=q.top();
		  		q.pop();
		  		if(t.second==n) continue;
		  		q.push({t.first-a[t.second]+a[t.second+1],t.second+1});
		  		q.push({t.first+a[t.second+1],t.second+1});
		  	}
		  	cout<<t.first;
		  	return 0;
		  }
		  ```
	- 思路2
		- 从小到大排序，二分答案，用一个队列记住当前的有效状态，一个状态包括当前的集合的和以及当前集合选择的数的最大编号。每次从队列里面取出一个状态，然后添加一个数，这个数的编号要大于最大编号，而且加上那个数的和要小于等于二分的答案，看总共有多少个集合的和小于等于二分的答案。
		-
- ##