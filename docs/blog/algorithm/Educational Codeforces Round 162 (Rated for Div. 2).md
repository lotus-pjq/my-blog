---
title: Educational Codeforces Round 162 (Rated for Div. 2)
date: 2025-10-14
category: 题解
tags:
  - 算法
outline: deep
---

## C #构造 #贪心- 题目- - 
- 思路
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i>n>>q;
int sum=0;
rep(i,1,n){
cin>>c[i];
if(c[i]==1) cnt1[i]=cnt1[i-1]+1;
else cnt1[i]=cnt1[i-1];
c[i]+=c[i-1];
}
int l,r;
rep(i,1,q){
cin>>l>>r;
if(r==l) cout=r-l+1+cnt1[r]-cnt1[l-1]) cout>t;
while(t--) solve();
return 0;
}
```
## D #二分
- 题目
- 思路
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i=i使得a[j]!=a[i]
bool check_l(int x,int pos){
  if(pos==1) return false;
  // 检查从x到pos-1的区间和是否大于a[pos]，并且x和pos-1之间有至少一个不同的值
    // 或者x和pos相邻且a[x]>a[pos]
  if(x==pos-1) return a[x]>a[pos];
    return (s[pos-1]-s[x-1]>a[pos])&&(f[x]a[pos]
  if(x==pos+1) return a[x]>a[pos];
    return (s[x]-s[pos]>a[pos])&&(f[pos+1]>n;
  rep(i,1,n) cin>>a[i];
  rep(i,1,n) s[i]=s[i-1]+a[i];
  // 预处理f数组：记录连续相同值的右边界
  for(int l=1,r;l1&&a[i-1]>a[i]) ans=min(ans,1LL);
        if(ia[i]) ans=min(ans,1LL);
    // 左边
    int l=1,r=i-1,mid,l_ans=-1,r_ans=-1;
    while(l>1;
      if(check_l(mid,i)) l=mid+1,l_ans=mid;
      else r=mid-1;
    }
    if(l_ans!=-1) ans=min(ans,i-l_ans);
    // 右边
    l=i+1,r=n;
    while(l>1;
      if(check_r(mid,i)) r=mid-1,r_ans=mid;
      else l=mid+1;
    }
    if(r_ans!=-1) ans=min(ans,r_ans-i);
    if(ans==INF) cout>t;
    while(t--) solve();
    return 0;
}
```