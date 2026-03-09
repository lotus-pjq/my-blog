---
title: Educational Codeforces Round 159 (Rated for Div. 2)
date: 2025-10-28
category: 数论
tags:
  - 算法
outline: deep
---

## B #二分 #贪心
- 题目- 
- 思路- 
- 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
int task,n,p,L,t;
int cal(int k){return k*L+min(2*k,task)*t;}
void solve(){
  cin>>n>>p>>L>>t;
  task=(n+6)/7;
  int l=0ll,r=n,ans;
  while(l>1;
    if(cal(mid)>=p) ans=mid,r=mid-1;
    else l=mid+1; 
  }
  cout>t;
    while(t--) solve();
    return 0;
}
```
## C #数论 #gcd #差分
- 题目- 
- 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
const int N=2e5+5;
int a[N],dif[N];
bool cmp(int x,int y){return x>y;}
int T=0;
const int M=262143;
struct E{int v;E*nxt;}*g[M+1],pool[N],*cur=pool,*p;int vis[M+1];
void ins(int v){
  int u=v&M;
  if(vis[u]nxt) if(p->v==v) return;
  p=cur++;p->v=v;p->nxt=g[u];g[u]=p;
}
bool ask(int v){
  int u=v&M;
  if(vis[u]nxt) if(p->v==v) return 1;
  return 0;
}
void init(){T++,cur=pool;}
void solve(){
  int n;cin>>n;
  init();
  for(int i=1;i>a[i],ins(a[i]);
  if(n==1){cout>t;
    while(t--) solve();
    return 0;
}
```
- 不同hash的时间- 