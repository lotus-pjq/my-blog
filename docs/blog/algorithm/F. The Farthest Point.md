---
title: F. The Farthest Point
date: 2026-03-09
category: 题解
tags:
  - 算法
outline: deep
---

## 题目：- # P12783 [ICPC 2024 Yokohama R] The Farthest Point
- ## 题目背景
	  
	  译自 [ICPC 2024 Yokohama Regional Contest](https://icpc.jp/2024/)。
- ## 题目描述
	  
	  一只蚂蚁位于一个长方体的顶点之一，记作**起始顶点**。长方体（rectangular cuboid）是一个所有面均为矩形的六面体。对于这只蚂蚁而言，长方体的表面就构成了它的整个「世界」。
	  
	  
	  现在我们想知道：在长方体表面上，哪个点对于蚂蚁来说距离起始顶点最远。你可能会认为，**对角顶点**（即起始顶点的空间对角线的另一端顶点）就是最远的点。然而，对角顶点并不一定是最远的。
	  
	  
	  例如，对于一个尺寸为 $1 \times 1 \times 2$ 的长方体，其任一顶点到对角顶点的表面距离为 $\sqrt{8}$。而实际上，最远点到起始顶点的距离为 $\sqrt{\tfrac{65}{8} }$（见下图）。
	  
	  > 
	  > （$1\times 1\times 2$ 的长方体，和长方体的展开图）
	  
	  现在给出长方体的边长尺寸。请编写一个程序，计算起始顶点到最远点的距离。
- ## 输入格式
	  
	  仅一组数据，格式如下所示：
	  
	  > $a$ $b$ $c$
	  
	  正整数 $a,b,c$ 表示长方体尺寸为 $a\times b\times c$。保证 $1\le a,b,c\le 100$。
- ## 输出格式
	  
	  输出一行一个实数，表示起始顶点到最远点的距离。相对误差不应大于 $10^{-9}$。
- ## 输入输出样例1
- ### 输入1
	  ```
	  1 1 2
	  ```
- ### 输出1
	  ```
	  2.850438562747845
	  ```
- ## 输入输出样例2
- ### 输入2
	  ```
	  10 10 10
	  ```
- ### 输出2
	  ```
	  22.360679774997898
	  ```
- ## 输入输出样例3
- ### 输入3
	  ```
	  100 2 3
	  ```
- ### 输出3
	  ```
	  101.0503923792481
	  ```
- ## 输入输出样例4
- ### 输入4
	  ```
	  2 3 5
	  ```
- ### 输出4
	  ```
	  7.093659140387279
	  ```
- ## 输入输出样例5
- ### 输入5
	  ```
	  84 41 51
	  ```
- ### 输出5
	  ```
	  124.582755157578
	  ```
- ## Code1(标答思路1):

```C++
	  #include
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const double PI=acos(-1);
	  #define double long double
	  struct point{
	      double x,y;
	      point(double x, double y):x(x),y(y){}
	      point():x(0),y(0){}
	  }p[4];
	  point operator+(point a,point b){return point(a.x+b.x,a.y+b.y);}
	  point operator-(point a,point b){return point(a.x-b.x,a.y-b.y);}
	  point operator*(point a,double t){return point(a.x*t,a.y*t);}
	  point operator/(point a,double t){return point(a.x/t,a.y/t);}
	  double operator*(point a,point b){return a.x*b.y-a.y*b.x;}//叉积
	  double operator&(point a,point b){return a.x*b.x+a.y*b.y;}//点积
	  double _k(point x){return -x.x/x.y;}
	  double dis(point a,point b){return sqrtl((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));}
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	int t[4];cin>>t[1]>>t[2]>>t[3];
	  	sort(t+1,t+4);double a=t[1],b=t[2],c=t[3];
	  	if(a==b&&b==c){cout
	  #define ld long double
	  using namespace std;
	  const ld eps=1e-9;
	  ld a,b,c;
	  ld getans(ld x,ld y){
	  	ld p1=(a+y)*(a+y)+(a+c-x)*(a+c-x);
	  	ld p2=x*x+(c+y)*(c+y);
	  	ld p3=y*y+(c+x)*(c+x);
	  	ld p4=(b+x)*(b+x)+(b+c-y)*(b+c-y);
	  	return min({p1,p2,p3,p4});
	  }
	  signed main(){
	  	cin>>a>>b>>c;
	  	if(b>c) swap(b,c);
	  	if(a>b) swap(a,b);
	  	if(b>c) swap(b,c);
	  	ld lx=0,rx=a,ly,ry;
	  	while(abs(rx-lx)>eps){
	  		ld dx=(rx-lx)/3, x1=lx+dx, x2=x1+dx;
	  
	  		ly=0,ry=b;
	  		while(abs(ry-ly)>eps){
	  			ld dy=(ry-ly)/3, y1=ly+dy, y2=y1+dy;
	  			ld s1=getans(x1,y1),s2=getans(x1,y2);
	  			if(s1eps){
	  			ld dy=(ry-ly)/3, y1=ly+dy, y2=y1+dy;
	  			ld s1=getans(x2,y1),s2=getans(x2,y2);
	  			if(s1<s2) ly=y1;
	  			else ry=y2;
	  		}
	  		ld s4=getans(x2,ly);
	  
	  		if(s3<s4) lx=x1;
	  		else rx=x2;
	  	}
	  	printf("%.14Lf",sqrtl(max(getans(lx,ly),getans(a,b))));
	  }
	  ```