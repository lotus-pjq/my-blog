---
title: 数位DP
date: 2025-10-23
category: 动态规划
tags:
  - 算法
outline: deep
---

### P2657 [SCOI2009] windy 数- 题目- # P2657 [SCOI2009] windy 数
  ## 题目背景
**本题与 [P13085 [SCOI2009] windy 数（加强版）](https://www.luogu.com.cn/problem/P13085) 的区别在于 $\bm{a}$ 与 $\bm{b}$ 的范围。**
windy 定义了一种 windy 数。
  ## 题目描述
不含前导零且相邻两个数字之差至少为 $2$ 的正整数被称为 windy 数。windy 想知道，在 $a$ 和 $b$ 之间，包括 $a$ 和 $b$ ，总共有多少个 windy 数？
  ## 输入格式
输入只有一行两个整数，分别表示 $a$ 和 $b$。
  ## 输出格式
输出一行一个整数表示答案。
  ## 输入输出样例 1
  ### 输入 1
```
1 10
```
  ### 输出 1
```
9
```
  ## 输入输出样例 2
  ### 输入 2
```
25 50
```
  ### 输出 2
```
20
```
  ## 说明/提示
  #### 数据规模与约定
对于全部的测试点，保证 $1 \leq a \leq b \leq 2 \times 10^9$。
- 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
int a,b,s[11],dp[11][11][2][2],len,cnta,cntb;
int dfs(int pos,int pre,bool frt0,bool lim){
  if(pos=2) res+=dfs(pos-1,i,frt0&&(i==0),lim&&(i==up));
  return dp[pos][pre][frt0][lim]=res;
}
void init(int x){
  len=0;
  memset(dp,-1,sizeof(dp));
  while(x){s[++len]=x%10;x/=10;}
}
signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
  cin>>a>>b;
  init(a-1);
  cnta=dfs(len,-1,1,1);
  init(b);
  cntb=dfs(len,-1,1,1);
  cout
using namespace std;
#define int long long
#define endl '\n'
int n,k;
int len,s[61],dp[61][61][2][2];
int dfs(int pos,int cnt,bool frt0,bool lim){
  if(pos>=1;}
}
signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
  cin>>n>>k;
  init(n);
  cout
using namespace std;
#define int long long
#define endl '\n'
int s[32],len,dp[32][32][32][2][2];
void init(int x){
  len=0;
  memset(dp,-1,sizeof(dp));
  while(x){s[++len]=x&1,x>>=1;}
}
int dfs(int pos,int cnt1,int cnt0,bool frt0,bool lim){
  if(pos=cnt1;
  if(~dp[pos][cnt1][cnt0][frt0][lim]) return dp[pos][cnt1][cnt0][frt0][lim];
  int res=0,up=lim?s[pos]:1;
  for(int i=0;i>l>>r;
  int cntl,cntr;
  init(l-1);
  cntl=dfs(len,0,0,1,1);
  init(r);
  cntr=dfs(len,0,0,1,1);
  cout
using namespace std;
#define int long long
#define endl '\n'
const int N=1e5+5,M=32,mod=998244353;
int n,a[N],l[N],s[M],jud[M],dp[M][2][2];
int len1,len2,len,ans;
int dfs(int pos,bool frt0,bool lim){
  if(pos0){s[++len1]=x&1,x>>=1;}
  len2=0;while(A>0){jud[++len2]=A&1,A>>=1;}
  ans*=dfs(len1,1,1);
  ans%=mod; 
}
void solve(){
  ans=1;
  cin>>n;
  for(int i=1;i>a[i];
  for(int i=1;i>l[i];
  for(int i=1;i>t;
  while(t--) solve();
  return 0;
}
```
```
```