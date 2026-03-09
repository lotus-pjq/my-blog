---
title: LCA
date: 2025-08-26
category: 图论
tags:
  - LCA
  - 图论
  - 技巧/倍增
  - 数据结构/ST表
  - 模板
outline: deep
---

## 倍增法（ST表）求LCA
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
const int N=5e5+5;
int n,m,root,dep[N],st[N][20];
vector e[N];
void dfs(int u,int fa){
dep[u]=dep[fa]+1;
st[u][0]=fa;
for(int i=1;i=0;i--)
if(dep[st[a][i]]>=dep[b])
a=st[a][i];	
if(a==b) return a;
for(int i=19;i>=0;i--)
if(st[a][i]!=st[b][i])
a=st[a][i],b=st[b][i];
return st[a][0];
}
signed main(){
ios::sync_with_stdio(false);
cin.tie(nullptr);
cin>>n>>m>>root;
int u,v;
for(int i=1;i>u>>v;
e[u].push_back(v);
e[v].push_back(u);
}
dfs(root,0);
for(int i=1;i>u>>v;
cout<<query(u,v)<<endl;
}
}
```
## Tarjan求LCA
```
```