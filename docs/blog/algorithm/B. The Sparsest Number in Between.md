---
title: B. The Sparsest Number in Between
date: 2026-03-09
category: 题解
tags:
  - 算法
outline: deep
---

## 题目：- # P12779 [ICPC 2024 Yokohama R] The Sparsest Number in Between
- ## 题目背景
	  
	  译自 [ICPC 2024 Yokohama Regional Contest](https://icpc.jp/2024/)。
- ## 题目描述
	  
	  给定一对正整数 $a,b$（$a \le b$）。在 $a$ 和 $b$ 之间（包括 $a$ 和 $b$）的整数中，你的任务是找到最**稀疏**的一个，即其二进制表示中 $\texttt{1}$ 的数量最少的一个。如果存在两个或更多这样的整数，你应该找到其中最小的一个。
	  
	  例如，假设 $a = 10$ 且 $b = 13$。 $a$ 和 $b$ 之间（包括 $a$ 和 $b$）的整数是 $10$、$11$、$12$ 和 $13$，它们的二进制表示分别为 $\texttt{1010},\texttt{1011},\texttt{1100}$ 和 $\texttt{1101}$。因此，在这种情况下，答案是 $10$，因为 $10$ 和 $12$ 的二进制表示中 $1$ 的数量最少，并且 $10$ 小于 $12$。
- ## 输入格式
	  仅一组数据，格式如下所示：
	  > $a$ $b$
	  其中，$a,b$ ($a \le b$) 是介于 $1$ 和 $10^{18}$ 之间（包括 $1$ 和 $10^{18}$）的整数。
- ## 输出格式
	  
	  输出一行一个整数，表示 $a$ 和 $b$ 之间（包括 $a$ 和 $b$）最稀疏整数中最小的一个。
- ## 输入输出样例 1
- ### 输入 1
	  
	  ```
	  10 13
	  ```
- ### 输出 1
	  
	  ```
	  10
	  ```
- ## 输入输出样例 2
- ### 输入 2
	  
	  ```
	  11 15
	  ```
- ### 输出 2
	  
	  ```
	  12
	  ```
- ## 输入输出样例 3
- ### 输入 3
	  
	  ```
	  11 20
	  ```
- ### 输出 3
	  
	  ```
	  16
	  ```
- ## 输入输出样例 4
- ### 输入 4
	  
	  ```
	  1 1000000000000000000
	  ```
- ### 输出 4
	  
	  ```
	  1
	  ```
- ## 输入输出样例 5
- ### 输入 5
	  
	  ```
	  9876543210 9876543210
	  ```
- ### 输出 5
	  
	  ```
	  9876543210
	  ```
- ## Code：

```C++
	  #include
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	int a,b,pos=0,ans=0;
	  	cin>>a>>b;
	  	for(int i=63;i>=0;i--){
	  		if((a>>i&1)!=(b>>i&1)){pos=i;break;}
	  		ans+=(a>>i&1)=a){
	  			cout<<ans+(1ll<<i);
	  			break;
	  		}
	  	return 0;
	  }
	  ```