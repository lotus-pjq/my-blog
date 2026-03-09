---
title: 最长公共子串(LCS)
date: 2025-08-30
category: 动态规划
tags:
  - 算法
outline: deep
---

## 最长公共子串(Longest Common Substring)
## 分析：
## Code1:只输出最长长度
```C++
#include
using namespace std;
string a,b;
int n,m,f[201][201];
signed main(){
cin>>n>>m>>a>>b;
a=' '+a;b=' '+b;
int ans=0;
for(int i=1;i
using namespace std;
string a,b;
int n,m,f[201][201];
signed main(){
cin>>n>>m>>a>>b;
a=' '+a;b=' '+b;
int len=0,pos=-1;
for(int i=1;ilen){
len=f[i][j];
pos=i;
}
}
cout<<len<<endl;
for(int i=pos-len+1;i<=pos;i++) cout<<a[i];
return 0;
}
```
```
```