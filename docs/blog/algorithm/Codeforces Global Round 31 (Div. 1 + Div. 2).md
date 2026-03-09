---
title: Codeforces Global Round 31 (Div. 1 + Div. 2)
date: 2025-12-20
category: 数学
tags:
  - 算法
outline: deep
---

## E.No Effect XOR #分治 #builtin #位运算 #剪枝
## 1. 问题简述
给定区间 $[l, r]$，求有多少个正整数 $x$，使得对于区间内任意整数 $i \in [l, r]$，满足 $i \oplus x \in [l, r]$。
换句话说，求使得区间 $[l, r]$ 在异或 $x$ 作用下保持封闭的 $x$ 的数量。
## 2. 核心思路：位运算与分治
  ### 2.1 异或的几何性质
  - 异或运算是对合变换。寻找合法的 $x$ 实际上是在寻找维持区间结构不变的变换。
观察区间的二进制特征：对于区间 $[l, r]$，找到 $l$ 和 $r$ 的二进制表示中最高不同位(MSB），记为第 $k$ 位。
  - ==k = 63 - __builtin_clzll( l^r );==
  - $l$ 的第 $k$ 位必然是 $0$，$r$ 的第 $k$ 位必然是 $1$。
  - 高于 $k$ 的所有位，$l$ 和 $r$ 均相同。
根据第 $k$ 位，我们可以将区间划分为两个子区间：
    - 其中分界点 $m$ 的计算方式为：保留 $r$ 的高位，第 $k$ 位置 $1$，低位全清零。
即==m = r&~((1ll
using namespace std;
#define int long long
#define endl '\n'
int solve(int l,int r){
if(l==r) return 1;
int k=63-__builtin_clzll(l^r);
if((r-l+1)==(1ll>t;
while(t--){
int l,r;cin>>l>>r;
cout<<solve(l,r)-1<<endl;
}
return 0;
}
```
```