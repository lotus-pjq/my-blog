---
title: 最长公共子序列(LCS)
date: 2025-08-30
category: 动态规划
tags:
  - 算法
outline: deep
---

## 给定两个字符串，给出其最长公共子序列的长度(Longest Common Sequence)。
## 分析：
## Code1:只求长度

```C++
#include
using namespace std;
const int N=1010;
int n,m;
char a[N], b[N];
int f[N][N];
int main(){
  cin>>n>>m>>a+1>>b+1;
  for(int i=1; i
using namespace std;
const int N=1e3+5;
int n,m,p[N][N];
char s[N];
string a,b;
int f[N][N];
signed main(){
  cin>>n>>m>>a>>b;
  a=' '+a; b=' '+b;
  for(int i=1;if[i-1][j]){
        f[i][j]=f[i][j-1];
        p[i][j]=2;//左边
      }else{
        f[i][j]=f[i-1][j];
        p[i][j]=3;//上方
      }     
    }

  int i=m,j=n,k=f[m][n];
  while(i>0&&j>0){
    if(p[i][j]==1){
      s[k--]=a[i];
      i--;j--;
    }else if(p[i][j]==2) j--;
    else i--;
  }
  cout<<f[n][m]<<endl;
  for(i=1;i<=f[m][n];i++) cout<<s[i];
}
```
```
```