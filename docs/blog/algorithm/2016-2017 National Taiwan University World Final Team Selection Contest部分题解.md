---
title: 2016-2017 National Taiwan University World Final Team Selection Contest部分题解
date: 2025-10-15
category: 数据结构
tags:
  - 算法
outline: deep
---

- PDF
- [national-taiwan-university-world-final-team-selection-contest-en.pdf](https://codeforces.com/gym/101234/attachments/download/5080/national-taiwan-university-world-final-team-selection-contest-en.pdf)
- ## A #二分答案 #线段树
- 题目(2016-2017 National Taiwan University World Final Team Selection Contest --- A)- 
- 题意描述
  - 给定一个长度为n的序列a, 有m次操作，每次操作选择一个区间[L,R], 将区间内的数从小到大排序，或从大到小排序，问最终序列中间的数是什么。
- 思路
  - 二分答案mid，将小于mid的数变成−1，大于mid的数变成1，等于mid的数为0，每次操作相当于询问某个区间内−1或1的个数，然后将区间重新染色，这个可以用线段树维护。最终如果中间的数是0，则二分的值就是答案，如果是−1说明答案偏大，否则答案偏小。
  - 时间复杂度: O(n\*logn\*logn)
- 代码

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i>1),build(rs,(l+r>>1)+1,r);
		  	up(x);
		  }
		  void update(int x,int l,int r,int val){
		  	if(t[x].l>r||t[x].r=l&&t[x].rr||t[x].r=l&&t[x].r>n>>k;
		  	rep(i,1,n) cin>>a[i];
		  	rep(i,1,k) cin>>ql[i]>>qr[i];
		  	int l=1,r=n,mid,ans;
		  	while(l>1;
		  		build(1,1,n);
		  		int cnt_neg,cnt_zero,cnt_pos;
		  		for(int i=1,l,r;i
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  #define pii pair
		  int n,m,a[N];
		  priority_queue,greater> q;
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n>>m;
		  	for(int i=1;i>a[i];
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
- 思路2- 从小到大排序，二分答案，用一个队列记住当前的有效状态，一个状态包括当前的集合的和以及当前集合选择的数的最大编号。每次从队列里面取出一个状态，然后添加一个数，这个数的编号要大于最大编号，而且加上那个数的和要小于等于二分的答案，看总共有多少个集合的和小于等于二分的答案。
		-
- ##