---
title: 2018ICPC_WF
date: 2025-10-26
category: 题解
tags:
  - 算法
outline: deep
---

## H. Single Cut of Failure
- 题目- 
- 思路
  - 首先答案必然小于等于2，那么只需要判断一次切割可不可行即可。
  - 将正方形看成一个圆环，只需要判断是否存在一个长为n的窗口$[l,r]$恰好包含n个线段的其中一个端点。
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
const int N=2e6+5;
int n,m,k,w,h,x,y;
int a[Nt.y;
else return x>t.x;
}
}p[N>n>>w>>h;
m=n>p[i*2-1].x>>p[i*2-1].y;
p[i*2-1].id=i;
p[i*2-1].tp=gettp(p[i*2-1].x,p[i*2-1].y);
cin>>p[i>p[i<<1].y;
p[i<<1].id=i;
p[i<<1].tp=gettp(p[i<<1].x,p[i<<1].y);
}
sort(p+1,p+m+1);
for(int i=1;i<=m;i++) a[i]=p[i].id;
int cnt=0;
int l=1,r=n,ansl=-1,ansr=-1;
for(int i=1;i<=n;i++){
if(!vis[a[i]]) cnt++;
vis[a[i]]++;
}
for(int i=1;i<=m;i++){
r=r%m+1;
if(!vis[a[r]]) cnt++;
vis[a[r]]++;
vis[a[l]]--;
if(!vis[a[l]]) cnt--;
l=l%m+1;
if(cnt==n){
ansl=l-1,ansr=r;
if(!ansl) ansl+=m;
break;
}
}
if(ansl!=-1){
cout<<1<<endl;
double x,y;
int tp1=p[ansl].tp;
if(tp1==1) x=0,y=p[ansl].y+0.5;
if(tp1==2) x=p[ansl].x+0.5,y=h;
if(tp1==3) x=w,y=p[ansl].y-0.5;
if(tp1==4) x=p[ansl].x-0.5,y=0;
cout<<fixed<<setprecision(6)<<x<<" "<<y<<" ";
int tp2=p[ansr].tp;
if(tp2==1) x=0,y=p[ansr].y+0.5;
if(tp2==2) x=p[ansr].x+0.5,y=h;
if(tp2==3) x=w,y=p[ansr].y-0.5;
if(tp2==4) x=p[ansr].x-0.5,y=0;
cout<<fixed<<setprecision(6)<<x<<" "<<y<<endl;
}else{
cout<<2<<endl;
cout<<"0 0.1 "<<w<<" "<<h-1<<".9"<<endl;
cout<<"0.1 "<<h<<" "<<w-1<<".9 0"<<endl;
}
return 0;
}
```
```
```