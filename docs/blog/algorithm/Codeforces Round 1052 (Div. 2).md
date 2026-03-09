---
title: Codeforces Round 1052 (Div. 2)
date: 2025-09-23
category: 题解
tags:
  - 算法
outline: deep
---

## B #贪心- ### 题目：- 
### hint：- 
### tutorial：- 
### 代码:
```C++
#include
using namespace std;
#define rep(i,j,k) for (int i=j;i>n>>m;
vector a[n];
for(int i=1;i>num;a[i].pb(num);
while(num--){
cin>>tmp;
a[i].pb(tmp);
vis[tmp]++;
}
}
bool flag=true;
for(int i=1;i=2){cout>t;
while(t--) solve();
return 0;
}
```
## D1 #按位- 题目：
- Tip：
  - 考虑“或运算”可以转换到可以“与运算”上。
==A&B + A|B = A+B==
- 思路：
- 代码：
```C++
#include
using namespace std;
#define INF 0x3f3f3f3f3f3f3f3f
const int N=2e5+5;
int ans[N];
void solve(){
  int l,r;cin>>l>>r;
  for(int i=l;i s;
  for(int i=l;i=l;i--){
    while(s.count(pw-i)==0) pw>>=1;
    ans[i]=pw-i;
    sum+=i|ans[i];
    s.erase(pw-i);
  } 
  cout>t;
  while(t--) solve();
  return 0;
}
```
## D2 #按位
- 题目：
- 思路：
- 代码：
```C++
#include
using namespace std;
const int N=2e5+5;
#define int long long
#define endl '\n'
int n,m,a[N];
int L,R;
void sol(int l,int r){
if(l>r) return;
if(l==r){a[l-L]=r;return;}
int tmp=l^r,pos=30;
while(pos>0&&(l>>pos&1)==(r>>pos&1)) pos--;
int mid=(r>>pos)=l&&tr+1>L>>R;
n=R-L+1;
sol(L,R);
int ans=0;
for(int i=0;i>t;
while(t--) solve();
return 0;
}
```
```
```