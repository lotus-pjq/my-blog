---
title: P13755 【MX-X17-T4】Yet another Game problem
date: 2025-08-19
category: 题解
tags:
  - 算法
outline: deep
---

- 题目：- # P13755 【MX-X17-T4】Yet another Game problem
## 题目描述
Alice 和 Bob 又在玩游戏。有一个序列 $a_1,a_2,\ldots,a_n$ 和一个区间 $[l,r]$ 初始为 $[1,n]$。双方都知道所有的信息，Alice 和 Bob 将轮流对这个区间进行操作，Alice 先手。
- 若轮到 Alice 操作，她可以选择一个 $i$（$l首先有一个显然的思路：就是二分 mid
把>=mid 设为 1，=0 的个数
那么当 Alice 修改成这个后缀之后，然后就赢了（注意到这个后缀是从后往前第一个符合要求的）
第二个不行，所有前缀都满足 1 的个数>=0 的个数，这样意味着 Bob 第二手已经找不到符号要求的前缀了
然后知道这个之后，就可以先二分，得出答案
再check 每个后缀 Bob 先手能不能胜
- 题解：
- Code：
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define INF 0x3f3f3f3f3f3f3f3f
#define rep(i,j,k) for (int i=j;i=k;--i)
const int N=1e6+5;
int a[N],n,op;
bool check(int x){
int cur=0;
per(i,n,2){
cur+=(x=0) return true;
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
while(l>1;
if(check(mid)) l=mid+1,ans=max(ans,mid);
else r=mid-1;
}
cout cho;
per(i,n,2){
cur+=(anslast) cho.push_back(i),last=cur,cnt++;
}
sort(cho.begin(),cho.end());
cout<<cnt<<endl;
for(int c:cho) cout<<c<<" ";
}
return 0;
}
```
```
```