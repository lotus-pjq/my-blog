---
title: FFT
date: 2026-03-09
category: 数学
tags:
  - 算法/FFT
  - 数学/多项式
  - 模板
description: FFT相关的算法笔记和代码模板
---

tags:: #算法/FFT #数学/多项式 #模板

- 模板：
  ```C++
  #include<bits/stdc++.h>
  using namespace std;
  #define int long long
  #define endl '\n'
  const int N=2e6+5;
  //FFT模板
  struct Complex{
  	double x,y;
  	Complex operator + (const Complex &w) const &{return (Complex){x+w.x,y+w.y};}
  	Complex operator - (const Complex &w) const &{return (Complex){x-w.x,y-w.y};}
  	Complex operator * (const Complex &w) const &{return (Complex){x*w.x-y*w.y,x*w.y+y*w.x};}
  }a[N],b[N];
  //空间要开比2*N的最小二的幂次，所以建议直接开N=4*N
  int r[N];
  int ans[N];
  void FFT(Complex a[],int n,int op){
  	for(int i=0;i<n;i++)
  		r[i]=(r[i>>1]>>1)+((i&1)?(n>>1):0);
  	for(int i=0;i<n;i++)
  		if(i<r[i]) swap(a[i],a[r[i]]);
  	for(int i=2;i<=n;i<<=1){
  		Complex w1({cos(2*PI/i),sin(2*PI/i)*op});
  		for(int j=0;j<n;j+=i){
  			Complex wk({1,0});
  			for(int k=j;k<j+i/2;k++){
  				Complex x=a[k],y=a[k+i/2]*wk;
  				a[k]=x+y;
  				a[k+i/2]=x-y;
  				wk=wk*w1;
  			}
  		}
  	}	
  }
  signed main(){
  	ios::sync_with_stdio(false);
  	cin.tie(nullptr);
  	int n,m;cin>>n>>m;
  	for(int i=0;i<=n;i++) cin>>a[i].x;
  	for(int i=0;i<=m;i++) cin>>b[i].x;
  	//m表示有值的最高位数，n表示大于等于m的最小二的幂次
  	for(m=n+m,n=1;n<=m;n<<=1);
  	//FFT 把a的系数表示转化为点值表示
  	FFT(a,n,1);
  	//FFT 把b的系数表示转化为点值表示 
  	FFT(b,n,1);
  	//FFT 两个多项式的点值表示相乘 
  	for(int i=0;i<n;i++) a[i]=a[i]*b[i];
  	//IFFT 把这个点值表示转化为系数表示 
  	FFT(a,n,-1);
  	//取实数四舍五入，此时虚数部分应当为0或由于浮点误差接近0
  	for(int i=0;i<n;i++) ans[i]+=(int)(a[i].x/n+0.5);
  	for(int i=0;i<=m;i++) cout<<ans[i]<<" ";
  	return 0;
  }
  ```