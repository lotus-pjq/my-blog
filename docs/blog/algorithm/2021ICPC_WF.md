---
title: 2021ICPC_WF
date: 2025-10-22
category: 数论
tags:
  - 算法
outline: deep
---

### C. Fair Division #gcd #数论 #等比数列
- 题目- 
- 思路
  - 第$$i$$位的价值是：$$m \cdot p \cdot \frac{(q-p)^{i-1} \cdot q^{n-i} }{q^n - (q-p)^n}$$
  - 要使得每一位都是整数的话必须使得 $$m\cdot p\%(q^n-(q-p)^n)==0$$
  - 附言：gcd(p,q)=1 ->gcd(q,q-p)=1
证明：gcd(q,q-p)=gcd(q,q-(q-p))=gcd(q,p)=1
- 代码
```C++
#include
using namespace std;
#define int long long 
#define endl '\n'
int gcd(int x,int y){
int tmp;
while(y!=0){tmp=x%y;x=y;y=tmp;}
return x;
}
__int128 ksm(__int128 a,int b){
__int128 res=1;
while(b){
if(b&1) res*=a;
a*=a;b>>=1;
}return res;
}
int n,mm;
__int128 m,fz,fm;//只存分子中需要判断取模部分
signed main(){
ios::sync_with_stdio(false);
cin.tie(0);
cin>>n>>mm;m=mm;
if(n>=61){coutm) break;
for(int p=1;p<q;p++){
fm=ksm(q,n)-ksm(q-p,n);
if(gcd(p,q)!=1) continue;
fz=m*p;
if(fz%fm==0){cout<<p<<" "<<q<<endl;return 0;}
}
}
cout<<"impossible"<<endl;
}
```
```
```