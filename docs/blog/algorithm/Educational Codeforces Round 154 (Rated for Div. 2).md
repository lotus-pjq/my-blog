---
title: Educational Codeforces Round 154 (Rated for Div. 2)
date: 2025-09-27
category: 题解
tags:
  - 算法
outline: deep
---

## B #构造- 题目
- 思路：
  > 考虑到分成两段
然后不要想着把一个变成另一个,把他们俩都变成同一个比如说000000111111
抓住这个开头是0结尾是1来构造
那就是找是否有相同位置的01就可以了
- 代码
```C++
#include
using namespace std;
#define endl '\n'
void solve(){
string a,b;cin>>a>>b;
int n=a.size();a=' '+a;b=' '+b;
bool f=0;
for(int i=1;i>t;
while(t--) solve();
return 0;
}

```
## C #模拟
- 题目- 
- 思路1代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
const int INF=1e18;
void solve(){
int l=1,r=INF,p=0;
string s;cin>>s;
for(int i=0;i=p){cout>t;
while(t--)solve();
return 0;
}

```
- 思路2
## D #DP
- 题目- 
- 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;ia[i-1]){
dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
dp[i][0]=dp[i-1][0]+1;
}else if(a[i]>n;
rep(i,1,n) cin>>a[i];
rep(i,2,n){
if(a[i]>a[i-1]){
dp[i][1]=min(dp[i-1][1],dp[i-1][0]+1);
dp[i][0]=dp[i-1][0]+1;
}else if(a[i]>t;
while(t--) solve();
return 0;
}

```
```
```