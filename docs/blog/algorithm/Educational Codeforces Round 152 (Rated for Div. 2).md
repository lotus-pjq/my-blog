---
title: Educational Codeforces Round 152 (Rated for Div. 2)
date: 2025-09-25
category: 题解
tags:
  - 算法
outline: deep
---

## D #贪心- 题目：
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i>n;
rep(i,1,n) cin>>a[i];
for(int i=1;i1) vis[i-1]=1,used=0;
int l=i;
while(a[l]) vis[l]=1,l++;
if(used) vis[l]=1;
}
}
for(int i=1;i<=n;i++)
if(!vis[i]) ans++;
cout<<ans;
return 0;
}
```
```
```