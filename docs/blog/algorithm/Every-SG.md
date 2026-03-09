---
title: Every-SG
date: 2026-03-09
category: 博弈论
tags:
  - 算法
description: Every-SG相关的算法笔记和代码模板
---

## Every-SG :
- > **“多局游戏同时进行、且每回合必须对所有尚未结束的游戏都走一步”**
  **胜负只由“最后结束的那局游戏”决定**；其余规则与正常 SG 相同。
- ###   形式化定义
	- 有 **n 个独立的子游戏** 同时开局。
	- 每回合，**当前玩家必须给所有尚未结束的子游戏各走一步**。
	- 当某一子游戏结束时，它就不再被操作。
	- **整个游戏结束** ⇔ **所有子游戏结束**。
	- **胜负判定**：
	  **最后结束的那个子游戏的赢家就是整场赢家**。
- ###   一句话总结:
  > **Every-SG 要求“所有未结束子游戏都要走”，胜负由“最后结束的那局”决定；对每个状态额外维护 `step`，总胜负看最大 `step` 的奇偶性。**
- Every-SG游戏与普通SG游戏最大的不同就是它多了一维**时间**。
- ### 胜负定理：
  > **先手必胜 ⇔ 所有子游戏中最大的 step 值是奇数**
  （最后一步由先手落子）。
- 对于==SG值为0（必败）==的点，玩家想要尽快结束，故我们需要知道==最少==需要多少步才能走到结束，
  对于==SG值不为0（必胜）==的点，玩家想要拖时间，故我们需要知道==最多==需要多少步结束
- 这样我们用**step**变量来记录当前子游戏从目前状态到结束需要多少步。
- $$
  \operatorname{step}(u)=
  \begin{cases}
  0, & u\text{ 为终止状态}\\[6pt]
  \max_{\substack{v\,\text{为}\,u\,\text{的后继}\\ \operatorname{sg}(v)=0} }\bigl(\operatorname{step}(v)+1\bigr), & \operatorname{sg}(u)\neq 0\\[10pt]
  \min_{v\,\text{为}\,u\,\text{的后继} }\bigl(\operatorname{step}(v)+1\bigr), & \operatorname{sg}(u)=0
  \end{cases}
  $$
- 引入一道题：
	- ### P1290 欧几里德的游戏
		- #### 题目描述
		  欧几里德的两个后代 Stan 和 Ollie 正在玩一种数字游戏，这个游戏是他们的祖先欧几里德发明的。给定两个正整数 $M$ 和 $N$，从 Stan 开始，从其中较大的一个数，减去较小的数的正整数倍，当然，得到的数不能小于 $0$。然后是 Ollie，对刚才得到的数，和 $M,N$ 中较小的那个数，再进行同样的操作……直到一个人得到了 $0$，他就取得了胜利。下面是他们用 $(25,7)$ 两个数游戏的过程：
		- 初始：$(25,7)$；
		- Stan：$(11,7)$；
		- Ollie：$(4,7)$；
		- Stan：$(4,3)$；
		- Ollie：$(1,3)$；
		- Stan：$(1,0)$。
		  Stan 赢得了游戏的胜利。
		  现在，假设他们完美地操作，谁会取得胜利呢？
		- #### 输入格式
		  **本题有多组测试数据。**
		  第一行为测试数据的组数 $C$。
		  下面 $C$ 行，每行为一组数据，包含两个正整数 $M,N(M,N<2^{31})$。
		- #### 输出格式
		  对每组输入数据输出一行，如果 Stan 胜利，则输出 `Stan wins`；否则输出 `Ollie wins`。
		- ##### 输入 1
		  
		  ```
		  2
		  25 7
		  24 15
		  ```
		- ##### 输出 1
		  
		  ```
		  Stan wins
		  Ollie wins
		  ```
		  
		  $1 \leq C \leq 6$。
		- ---
	- 用SG函数打表观察：
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=20;
		  int sg[N+5][N+5];
		  void init(){
		  	for(int i=0;i<=N;i++)
		  		for(int j=0;j<=N;j++) sg[i][j]=-1;
		  	for(int i=0;i<=N;i++) sg[i][0]=sg[0][i]=0;
		  }
		  int SG(int x,int y){
		  	if(sg[x][y]!=-1) return sg[x][y];
		  	if(x>y) swap(x,y);
		  	int p=0;
		  	set<int> st;
		  	for(int i=1;i<=(y/x);i++)
		  		st.insert(SG(x,y-i*x));
		  	while(st.count(p)) p++;
		  	return sg[x][y]=sg[y][x]=p;
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	init();
		  	for(int i=1;i<=N;i++){
		  		for(int j=1;j<=i;j++)
		  			if(SG(i,j)==0) 
		  				cout<<"["<<i<<","<<j<<"]"<<"  ";
		  		cout<<endl;
		  	}
		  	return 0;
		  }
		  ```
		- >[3,2]  
		  [4,3]  
		  [5,4]  
		  [6,4]  [6,5]  
		  [7,5]  [7,6]  
		  [8,5]  [8,6]  [8,7]  
		  [9,6]  [9,7]  [9,8]  
		  [10,7]  [10,8]  [10,9]  
		  [11,7]  [11,8]  [11,9]  [11,10]  
		  [12,8]  [12,9]  [12,10]  [12,11]  
		  [13,9]  [13,10]  [13,11]  [13,12]  
		  [14,9]  [14,10]  [14,11]  [14,12]  [14,13]  
		  [15,10]  [15,11]  [15,12]  [15,13]  [15,14]  
		  [16,10]  [16,11]  [16,12]  [16,13]  [16,14]  [16,15]  
		  [17,11]  [17,12]  [17,13]  [17,14]  [17,15]  [17,16]  
		  [18,12]  [18,13]  [18,14]  [18,15]  [18,16]  [18,17]  
		  [19,12]  [19,13]  [19,14]  [19,15]  [19,16]  [19,17]  [19,18]  
		  [20,13]  [20,14]  [20,15]  [20,16]  [20,17]  [20,18]  [20,19]
	- 发现打表找不出什么规律捏！
	- ### （法一）如果有神秘观察力以及经验，会发现：
		- 20->13 , 19->12 , 18->12 , 17->11 , 16->10 , 15->10 , 14->9 ...
		- 看似有规律有无规律又有规律，实际上是惊人的 $A/B<(√5+1)/2$ 。
		- ```C++
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	long double cmp=(sqrtl(5)+1)/2;
		  	int t;cin>>t;
		  	double x,y;
		  	while(t--){
		  		cin>>x>>y;
		  		if(x<y) swap(x,y);
		  		if((x/y)<cmp&&x!=y) cout<<"Ollie wins"<<endl;
		  		else cout<<"Stan wins"<<endl; 
		  	}
		  	return 0;
		  }
		  ```
	- ### (法二)：
	- 于是考虑游戏玩法，考虑伪对称操作，或者说，让对方无法无法复刻的状态。
	- 考虑两个数A，B（A>B且不整除），要是A>2*B，只要对方不一次性把A变成==A'=A%B==，那么你就可以通过一次操作变成==A'=A%B+B==的状态。
	  那么下一次对方就一定会把==A'=A%B==。
	- 下面默认(x,y)中x>=y
		- 如果（A,B）中A>2*B到一下次除数改变的状态(B,A%B）时开局先手的人不会变，
		- 如果（A,B）中A%B=0，则先手必胜
		- 如果（A,B）中B<A<2*B则可以保证到一下次除数改变的状态(B,A%B）时开局先手的人改变。
		- ```C++
		  #include <cstdio>
		  #include <iostream>
		  using namespace std;
		  int m,n,q;
		  //当前操作者为p,p为0时代表Stan操作,p为1时代表Ollie操作。
		  int find(int x,int y,int p)
		  {
		  	if(x==y) return p;//返回胜者.
		  	if(y/x>=2) return p;//返回胜者.
		  	else return find(y-x,x,p^1);//向下一个状态查找.
		  }
		  int main(){
		  	cin>>q;
		  	for(int i=1;i<=q;i++){
		  		cin>>m>>n;
		  		if(m>n) swap(m,n);
		  		if(find(m,n,0)==0) cout<<"Stan wins"<<endl;
		  		else cout<<"Ollie wins"<<endl;
		  	}
		  	return 0;
		  	
		  }
		  ```
	-
	-
- ### HDU 3595
	- ### GG 和 MM
	  
	  时间限制：C++ 2000MS，其他语言 1000MS  
	  内存限制：Java 65536K，其他语言 32768K  
	  总提交次数：1650，接受的提交次数：701
	- #### 问题描述
	         GG 和 MM 从小喜欢玩游戏。游戏开始时，有两堆石头。MM 先选择一堆，这堆石头有 x 个石头，然后她可以选择一个正整数 k，从另一堆石头中移除 k*x 个石头（即 y = k*x）。然后轮到 GG 了，也遵循上述规则。当某人不能移除任何石头时，他/她就输了游戏，游戏结束。
	         多年后，GG 和 MM 发现这个游戏太简单了，于是他们决定一次玩 N 局来增添乐趣。MM 先开始，同样，轮到她/他时必须玩完所有未结束的游戏。移除规则与上述相同。如果某人无法移除任何石头（即输掉最后一局结束游戏），那么他/她就输了。当然，我们可以假设 GG 足够聪明，且 GG 不会故意放水。
	- #### 输入
	         输入包含多个测试用例（不超过 100 个）。
	         每个测试用例的第一行是一个整数 N，N <= 1000，表示有 N 场游戏。随后是 N 行，每行包含两个数：p 和 q，分别代表每场游戏中的两个石堆数目，p 和 q <= 1000（看起来它们真是悠闲 =-！），代表每场游戏中的两个石堆数目。
	  输入将以 EOF 结束。
		- ---
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  int st[1000+8][1000+8]; //每个状态玩到最后的步数
	  int find(int a,int b) {
	      if(a==0||b==0) return 0;
	      if(a<b) swap(a,b);
	      if(st[a][b]!=-1) return st[a][b];
	      if(a%b==0) return st[a][b] = 1; 
	      int tem=find(a%b,b); // 记录 (a%b, b) 的步数
	      if(tem&1) st[a][b]=tem+2; // tem 为奇数，转到必败态
	      else st[a][b]=tem+1; //转到必胜态
	      return st[b][a]=st[a][b];
	  }
	  int main() {
	      int n;
	      memset(st,-1,sizeof(st)); //初始化状态数组
	      while(~scanf("%d",&n)&&n) {
	          int ans=0;
	          for(int i=1;i<=n;++i) {
	              int a,b;scanf("%d %d",&a,&b);
	              if(a==0||b==0) continue;
	              ans=max(ans,find(a,b)); //记录最多步数那个游戏
	          }
	          if(ans&1) puts("MM"); //奇数步MM胜
	          else puts("GG"); //偶数步GG胜
	      }
	      return 0;
	  }
	  ```
-