---
title: P13755 【MX-X17-T4】Yet another Game problem
date: 2026-03-09
category: 题解
tags:
  - 算法
description: P13755 【MX-X17-T4】Yet another Game problem相关的算法笔记和代码模板
---

- 题目：
	- # P13755 【MX-X17-T4】Yet another Game problem
	- ## 题目描述
	  Alice 和 Bob 又在玩游戏。有一个序列 $a_1,a_2,\ldots,a_n$ 和一个区间 $[l,r]$ 初始为 $[1,n]$。双方都知道所有的信息，Alice 和 Bob 将轮流对这个区间进行操作，Alice 先手。
	- 若轮到 Alice 操作，她可以选择一个 $i$（$l<i\le r$），并把区间变为 $[i,r]$。
	- 若轮到 Bob 操作，他可以选择一个 $i$（$l\le i< r$），并把区间变为 $[l,i]$。
	  当 $l=r$ 时，游戏结束。最终得分即为 $a_l$。
	  Alice 希望这个最终得分尽可能大，Bob 则希望最终得分尽可能小。假设双方都采用最优策略，请问最终得分会是多少？有时为了防止你蒙混过关，Alice 还要你告诉她第一步应该如何操作。
	- ## 输入格式
	  第一行，两个整数 $n, \mathit{op}$。若 $\mathit{op}=0$，你只需求出答案即可；否则，你还需求出第一步的方案。
	  第二行，$n$ 个正整数 $a_1,a_2,\ldots,a_n$。
	- ## 输出格式
	  第一行，一个正整数，表示最终得分。
	  若 $\mathit{op}=1$，则：
	  第二行，一个正整数 $k$，表示可能的第一步的数量。
	  第三行，$k$ 个正整数，表示 $k$ 种操作第一步的方法，按升序输出。
	- ## 输入输出样例 1
	- ### 输入 1
	  
	  ```
	  5 0
	  1 2 3 4 5
	  ```
	- ### 输出 1
	  
	  ```
	  5
	  ```
	- ## 输入输出样例 2
	- ### 输入 2
	  
	  ```
	  5 1
	  2 5 1 4 3
	  ```
	- ### 输出 2
	  
	  ```
	  4
	  1
	  4
	  ```
	- ## 说明/提示
	  **【样例解释 #1】**
	  Alice 可以直接把区间 $[1,5]$ 变成 $[5,5]$，最终得分为 5。显然没有比这更优的操作了。
	  **【样例解释 #2】**
	  Alice 先把区间 $[1,5]$ 变成区间 $[4,5]$，随后 Bob 把区间 $[4,5]$ 变成区间 $[4,4]$，最终得分为 4。可以证明这是唯一可能的操作过程。
	  **【数据范围】**
	  |测试点编号|$n$|$\mathit{op}$|
	  |:-:|:-:|:-:|
	  |$1\sim 4$|$\le 100$|$=0$|
	  |$5\sim 10$|$\le 3000$|$=0$|
	  |$11\sim 18$|$\le 10^6$|$=0$|
	  |$19\sim 20$|$\le 10^6$|$=1$|
	  对于 $100\%$ 的数据，$2\le n\le 10^6$，$\mathit{op} \in\{0,1\}$，$1 \le a_i \le 10^9$。
- 思路（xde）：
	- >首先有一个显然的思路：就是二分 mid
	  把>=mid 设为 1，<mid 设为 0
	  然后 Alice 希望是 1
	  我发现如果从后往前，找到了一个后缀，使得1 个数>=0 的个数
	  那么当 Alice 修改成这个后缀之后，然后就赢了（注意到这个后缀是从后往前第一个符合要求的）
	  第二个不行，所有前缀都满足 1 的个数>=0 的个数，这样意味着 Bob 第二手已经找不到符号要求的前缀了
	  然后知道这个之后，就可以先二分，得出答案
	  再check 每个后缀 Bob 先手能不能胜
- 题解：
	- 
	- 
	- 
- Code：
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  #define INF 0x3f3f3f3f3f3f3f3f
	  #define rep(i,j,k) for (int i=j;i<=k;++i)
	  #define per(i,j,k) for (int i=j;i>=k;--i)
	  const int N=1e6+5;
	  int a[N],n,op;
	  bool check(int x){
	  	int cur=0;
	  	per(i,n,2){
	  		cur+=(x<=a[i])?1:-1;
	  		if(cur>=0) return true;
	  	}
	  	return false;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	cin>>n>>op;
	  	int mn=INF,mx=0;
	  	rep(i,1,n) cin>>a[i],mx=max(mx,a[i]),mn=min(mn,a[i]);
	  	int l=mn,r=mx,mid,ans=-1;
	  	while(l<=r){
	  		mid=l+r>>1;
	  		if(check(mid)) l=mid+1,ans=max(ans,mid);
	  		else r=mid-1;
	  	}
	  	cout<<ans<<endl;
	  	if(op){
	  		int cnt=0,cur=0,last=-1;
	  		vector<int> cho;
	  		per(i,n,2){
	  			cur+=(ans<=a[i])?1:-1;
	  			if(cur>last) cho.push_back(i),last=cur,cnt++;
	  		}
	  		sort(cho.begin(),cho.end());
	  		cout<<cnt<<endl;
	  		for(int c:cho) cout<<c<<" ";
	  	}
	   	return 0;
	  }
	  ```