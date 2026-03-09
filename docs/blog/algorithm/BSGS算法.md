---
title: BSGS算法
date: 2025-10-21
category: 数论
tags:
  - 算法
outline: deep
---

## BSGS
### 分析
  #### 作用：求解高次同余方程 $$a^x≡b (mod p)$$的最小非负整数x，其中$$a,p$$互质
  #### 时间复杂度：O(√n)
  #### BSGS : Baby Step Giant Step
### 知识点
### 模版题 (P3846)
  - 题目- # P3846 [TJOI2007] 可爱的质数/【模板】BSGS
  ## 题目描述
给定一个质数 $p$，以及一个整数 $b$，一个整数 $n$，现在要求你计算一个最小的非负整数 $l$，满足 $b^l \equiv n \pmod p$。
  ## 输入格式
仅一行，有 $3$ 个整数，依次代表 $p, b, n$。
  ## 输出格式
仅一行，如果有 $l$ 满足该要求，输出最小的 $l$，否则输出 `no solution`。
  ## 输入输出样例 1
  ### 输入 1
```
5 2 3
```
  ### 输出 1
```
3
```
  ## 说明/提示
  #### 数据规模与约定
  - 对于所有的测试点，保证 $2\le b 
using namespace std;
#define int long long
#define endl '\n'
const int N=2e5+5;
//求同余方程a^x≡b (modp)的最小非负整数x,其中a,p互质
int BSGS(int a,int b,int p){
a%=p,b%=p;
if(b==1) return 0;//x=0
int m=ceil(sqrt(p));
// a^x≡b  a^(i*m-j)≡b  (a^m)^i≡b*a^j
int t=b,mi=1;
unordered_map hash;
hash[b]=0;
for(int j=1;j>p>>a>>b;
int res=BSGS(a,b,p);
if(res==-1) cout
using namespace std;
#define int long long
#define endl '\n'
int gcd(int a,int b){
int tmp;
while(b!=0){tmp=a%b;a=b;b=tmp;}
return a;
}
int EX_BSGS(int a,int b,int p){
a%=p,b%=p;
if(b==1||p==1) return 0;//x=0
int g,k=0,A=1;
while(true){
g=gcd(a,p);
if(g==1) break;
if(b%g) return -1;//显然无解
k++;
b/=g,p/=g;
A=A*(a/g)%p;//A=a^k/D
if(A==b) return  k;
}
int m=ceil(sqrt(p));
int t=b,mi=1;
unordered_map hash;
hash[b]=0;
for(int j=1;j>a>>p>>b&&a){
int res=EX_BSGS(a,b,p);//求满足 a^x=b(modp)的最小非负整数x
if(res==-1) cout<<"No Solution"<<endl;
else cout<<res<<endl;
}
return 0;
}

```
```