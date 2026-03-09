---
title: I. Greatest of the Greatest Common Divisors
date: 2026-03-09
category: 题解
tags:
  - 算法
description: I. Greatest of the Greatest Common Divisors相关的算法笔记和代码模板
---

## 题目：
	- # P12786 [ICPC 2024 Yokohama R] Greatest of the Greatest Common Divisors
	- ## 题目背景
	  
	  译自 [ICPC 2024 Yokohama Regional Contest](https://icpc.jp/2024/)。
	- ## 题目描述
	  
	  给定一个整数序列和该序列上的若干区间。这些区间由其最左位置和最右位置指定。一个包含 $k$ 个整数的区间具有 $k(k - 1)/2$ 个位于不同位置的数对，每个数对有其最大公约数。 对于每个给定的区间，找出所有这些最大公约数中最大的一个。  
	  
	  例如，当序列为 $(a_1, \ldots, a_6) = (10, 20, 30, 40, 50, 60)$，且询问区间为整个序列时，需要考虑以下 $15$ 个位于不同位置 $x$ 和 $y$ 的两个整数组成的数对及其最大公约数：
	  
	  
	  | $x$ | $1$ | $1$ | $1$ | $1$ | $1$ | $2$ | $2$ | $2$ | $2$ | $3$ | $3$ | $\textbf{3}$ | $4$ | $4$ | $5$ |
	  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | 
	  | $y$ | $2$ | $3$ | $4$ | $5$ | $6$ | $3$ | $4$ | $5$ | $6$ | $4$ | $5$ | $\textbf{6}$ | $5$ | $6$ | $6$ |
	  | $a_x$ | $10$ | $10$ | $10$ | $10$ | $10$ | $20$ | $20$ | $20$ | $20$ | $30$ | $30$ | $\textbf{30}$ | $40$ | $40$ | $50$ |
	  | $a_y$ | $20$ | $30$ | $40$ | $50$ | $60$ | $30$ | $40$ | $50$ | $60$ | $40$ | $50$ | $\textbf{60}$ | $50$ | $60$ | $60$ |
	  | $\gcd(a_x,a_y)$ | $10$ | $10$ | $10$ | $10$ | $10$ | $10$ | $20$ | $10$ | $20$ | $10$ | $10$ | $\textbf{30}$ | $10$ | $20$ | $10$ |  
	  
	  在此例中，这 $15$ 个数对的最大公约数中的最大值为 $\gcd(30, 60) = 30$。
	- ## 输入格式
	  
	  仅一组数据，格式如下所示：
	  
	  > $n$\
	  > $a_1$ $\cdots$ $a_n$\
	  > $q$\
	  > $l_1$ $r_1$\
	  > $\cdots$\
	  > $l_q$ $r_q$
	  
	  第一行包含一个整数 $n$，表示给定序列中整数的个数，满足 $2 \leq n \leq 10^5$。第二行包含 $n$ 个正整数 $a_1$ 到 $a_n$，指定该序列。其中每个数均不超过 $10^5$。  
	  
	  第三行包含一个正整数 $q$，指定要考虑的序列区间数量，其值不超过 $10^5$。  随后是 $q$ 行，每行指定序列中一个要考虑的区间。其中第 $i$ 行包含两个整数 $l_i$ 和 $r_i$ $(1 \leq l_i < r_i \leq n)$，指定序列中从 $a_{l_i}$ 到 $a_{r_i}$ 的区间。
	- ## 输出格式
	  
	  输出 $q$ 行，其中第 $i$ 行应包含在 $l_i$ 和 $r_i$ 指定的区间内所有数对的最大公约数中的最大值。
	- ## 输入输出样例1
	- ### 输入1
	  
	  ```
	  6
	  10 20 30 40 50 60
	  3
	  1 6
	  2 5
	  4 5
	  ```
	- ### 输出2
	  
	  ```
	  30
	  20
	  10
	  ```
	- ## 输入输出样例2
	- ### 输入2
	  
	  ```
	  10
	  13 2 35 4 13 2 5 1 7 4
	  5
	  1 4
	  4 10
	  3 8
	  3 9
	  1 10
	  ```
	- ### 输出2
	  
	  ```
	  2
	  4
	  5
	  7
	  13
	  ```
- ## Code:
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define pb push_back
	  #define endl '\n'
	  const int N=1e5+5;
	  int n,q,B,a[N],num[N],cnt[N];
	  vector<int>g[N];
	  struct node{
	      int l,r,id;
	  	bool operator<(const node&t)const{
	  		if(l/B!=t.l/B) return l<t.l;
	  		if((l/B)&1) return r<t.r;
	  		else return r>t.r;
	  	}
	  }p[N];
	  int mx=1;
	  void add(int x){
	      for(auto&op:g[x]){
	          num[op]++;
	          if(num[op]==2){
	              cnt[op]=1;
	              if(op>mx) mx=max(mx,op);
	          }
	      }
	  }
	  void del(int x){
	      for(auto&op:g[x]){
	          num[op]--;
	          if(num[op]==1){
	              cnt[op]=0;
	              if(op==mx)
	              for(int j=op-1;j>=1;j--)
	                  if(cnt[j]){mx=j;break;}
	          }
	      }
	  }
	  void init(){
	      for(int i=2;i<N;i++)
	          for(int j=i;j<N;j+=i)
	              g[j].push_back(i);
	  }
	  signed main(){
	      ios::sync_with_stdio(0);
	      cin.tie(0);cout.tie(0);
	  	init();
	  	cin>>n;
	      B=sqrt(n);
	      for(int i=1;i<=n;i++) cin>>a[i];
	      cin>>q;
	      for(int i=1;i<=q;i++){
	          cin>>p[i].l>>p[i].r;
	          p[i].id=i;
	      }
	      sort(p+1,p+q+1);
	      p[0].r=0;p[0].l=1;
	      int ans[q+1];
	      int l=1,r=0;
	      cnt[1]=1;
	      for(int i=1;i<=q;i++){
	          while(l>p[i].l) add(a[--l]);
	  		while(r<p[i].r) add(a[++r]);
	  		while(l<p[i].l) del(a[l++]);
	  		while(r>p[i].r) del(a[r--]);
	          ans[p[i].id]=mx;
	      }
	      for(int i=1;i<=q;i++) cout<<ans[i]<<endl;
	  }
	  ```