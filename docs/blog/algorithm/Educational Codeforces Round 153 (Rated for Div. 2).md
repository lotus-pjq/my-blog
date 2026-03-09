---
title: Educational Codeforces Round 153 (Rated for Div. 2)
date: 2025-09-26
category: 博弈论
tags:
  - 算法
outline: deep
---

## A #字符串 #构造- 题目
- 代码
```C++
#include
using namespace std;
#define rep(i,j,k) for (int i=j;i>s;
int n=s.size();
rep(i,1,n) a+='(';
rep(i,1,n) a+=')';
rep(i,1,n) b+="()";
if(s.size()==2&&s=="()") cout>t;
while(t--) solve();
return 0;
}
```
## B- 题目- 
- 代码

```C++
#include
using namespace std;
#define INF 0x3f3f3f3f3f3f3f3f
#define rep(i,j,k) for (int i=j;i>m>>k>>a1>>ak;
int take_k=m/k;
int take_1=m%k;
int take_fancy_1=max(0ll,take_1-a1);
int left_regular_1=max(0ll,a1-take_1);
int take_fancy_k=max(0ll,take_k-ak);
int replace=min(left_regular_1/k,take_fancy_k);
int ans=take_fancy_1+take_fancy_k-replace;
cout>t;
while(t--) solve();
return 0;
}
```
## C #博弈- 题目
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
const int N=3e5+5;
int n,m,a[N];
void solve(){
  cin>>n;
  int ans=0;
  int mn=n+1,mnWin=n+1,x;
  while(n--){
    cin>>x;
    if(mn>t;
  while(t--) solve();
  return 0;
}
```
## D #DP （？)
- 题目- 
- 思路- > 首先这题是个性质题目
- 题解- 
```C++
#include 
using namespace std;
using li = long long;
const int N = 111;

int n;
string s;
int dp[2][N][N * N];

int main() {
cin >> s;
n = s.size();
dp[0][0][0] = 0;
for (int i = 0; i < n; ++i) {
for (int j = 0; j <= i + 1; ++j) {
for (int cnt = 0; cnt <= j * (i + 1 - j); ++cnt) {
dp[1][j][cnt] = n;   
}
}
for (int j = 0; j <= i; ++j) {
for (int cnt = 0; cnt <= j * (i - j); ++cnt) {
dp[1][j + 1][cnt] = min(dp[1][j + 1][cnt], dp[0][j][cnt] + (s[i] != '0'));
dp[1][j][cnt + j] = min(dp[1][j][cnt + j], dp[0][j][cnt] + (s[i] != '1'));
}
} 
swap(dp[0], dp[1]);
}
int cnt0 = count(s.begin(), s.end(), '0');
cout << dp[0][cnt0][cnt0 * (n - cnt0) / 2] / 2 << '\n';
}
```