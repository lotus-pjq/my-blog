---
title: Educational Codeforces Round 164 (Rated for Div. 2)
date: 2025-10-17
category: 动态规划
tags:
  - 算法
outline: deep
---

## B- 题目
- 思路
  - 数列是好的  a1=an&&不存在i in [1,n-1]ai,ai+1!=an
结论：==等于a1,an的极长段的最小值==
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i>n;
rep(i,1,n) cin>>a[i];
a[0]=a[n+1]=-1;
if(a[1]!=a[n]){cout=n)?-1:ans)>t;
while(t--) solve();
return 0;
}

```
## D #DP #1800 #小结论 #背包- 题目- D. 彩色球  
每测试点时间限制：2秒  
每测试点内存限制：1024兆字节  

有n种不同颜色的球，第i种颜色的球的数量为ai。  
这些球可以被组合成若干组。每组最多包含2个球，且同组内每种颜色的球不超过1个。  
考虑所有2^n种颜色集合。对于一个颜色集合，其价值定义为该集合中所有颜色的球被分配到的最小组数。例如，假设有三种颜色的球数量分别为3、1和7，它们可以被组合成7组（且无法少于7组），因此该颜色集合的价值为7。  
你的任务是计算所有2^n种可能的颜色集合的价值之和。由于结果可能过大，请输出其对998244353取模的值。
  - 输入
  - 第一行包含一个整数n（1≤n≤5000）——颜色数量。  
第二行包含n个整数a1, a2, …, an（1≤ai≤5000）——每种颜色球的数量。  
输入额外限制：球的总数不超过5000。
  - 输出
  - 输出一个整数——所有2^n种颜色集合的价值之和，对998244353取模的结果。
  - 示例
  - 输入  
3  
1 1 2  
输出  
11
  - 输入  
1  
5  
输出  
5
  - 输入  
4  
1 3 3 7  
输出  
76
  - 说明
  - 以第一个示例为例。共有8种颜色集合：
  - 空集的价值为0；
  - 集合{1}的价值为1；
  - 集合{2}的价值为1；
  - 集合{3}的价值为2；
  - 集合{1,2}的价值为1；
  - 集合{1,3}的价值为2；
  - 集合{2,3}的价值为2；
  - 集合{1,2,3}的价值为2。  
因此，所有2^n种集合的价值总和为11。
- 小结论
  - 对于k个颜色，分别b1,b2,...,bk个球，将按照一个球或者两个球进行分组，但是一组中如果有两个球则两个颜色不能相同。
  - 最少要分多少组
  - Answer：min( ceil[(a1+a2+...+ak)/2] , max{bi} )  ceil()表示上取整
- 思路
  - 对a排序（从小到大)，f[i][j]表示前i个元素中选了j个小球的==方案数==。
  - 因为答案求的是贡献，要在每次统计是计算对应方法的贡献。
  - 初始化f[0][0]=1,sum=0;
  - 状态转移:
  - 0.统计答案,ans+=f[i-1][j]*max((j+1+a[i])/2,a[i])
  - 1.f[i][j]=f[i-1][j]
  - 2.f[i][j+a[i]]+=f[i-1][j];  j:0->sum
  - sum+=a[i]
- 代码

```C++
#include
using namespace std;
#define int long long
#define endl '\n'
const int N=5e3+5;
const int mod=998244353;
int n,a[N],f[2][N];
//f[i][j]:前i个元素里选了j个小球的方案数
signed main(){
ios::sync_with_stdio(false);
cin.tie(nullptr);
cin>>n;
for(int i=1;i>a[i];
sort(a+1,a+n+1);
f[0][0]=1;
int ans=0,sum=0;
for(int i=1;i<=n;i++){
for(int j=0;j<=sum;j++) f[i&1][j]=f[(i-1)&1][j];
for(int j=0;j<=sum;j++) ans+=f[(i-1)&1][j]*max((j+a[i]+1)/2,a[i])%mod;
for(int j=0;j<=sum;j++) f[i&1][j+a[i]]=(f[i&1][j+a[i]]+f[(i-1)&1][j])%mod;
sum+=a[i];
}
cout<<ans%mod;
}
```