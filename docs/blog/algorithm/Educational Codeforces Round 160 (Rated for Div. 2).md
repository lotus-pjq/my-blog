---
title: Educational Codeforces Round 160 (Rated for Div. 2)
date: 2025-10-17
category: 动态规划
tags:
  - 算法
outline: deep
---

## B
- 题目- 
- 思路- - 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i>s;
  int n=s.size();
  s=' '+s;
  for(int i=1;i>t;
    while(t--) solve();
    return 0;
}
```
## Ｃ #按位 #贪心 #1300- 题目- 
- 思路
  - 如果没有二进制的话就是背包。
  - 但有了二进制的组合后就可以贪心的取了
- 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i>n;
  memset(cnt,0,sizeof(cnt));
  rep(i,1,n){
    cin>>op>>x;
    if(op==1){cnt[x]++;}
    else{
      for(int i=30;i>=0;i--){
        int tmp=x/(1
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i0&&a[sta[pos]]>a[i]) pos--;
    if(pos>0) rs[sta[pos]]=i;
    if(posr) return 1;
  int ansl=dfs(l,x-1,ls[x],x);
  int ansr=dfs(x+1,r,rs[x],x);
  int res=ansl*ansr%mod;
  if(l>1) res+=ansr;
  if(r1&&r>n;
  rep(i,1,n) cin>>a[i];
  build();
  cout>t;
    while(t--) solve();
    return 0;
}

```
-