---
title: 字典树Trie
date: 2026-03-09
category: 数据结构
tags:
  - 算法
description: 字典树Trie相关的算法笔记和代码模板
---

- 又名“前缀树”
- 模板题（P8306）
	- 题目
		- # P8306 【模板】字典树
		- ## 题目描述
		  
		  给定 $n$ 个模式串 $s_1, s_2, \dots, s_n$ 和 $q$ 次询问，每次询问给定一个文本串 $t_i$，请回答 $s_1 \sim s_n$ 中有多少个字符串 $s_j$ 满足 $t_i$ 是 $s_j$ 的**前缀**。
		  
		  一个字符串 $t$ 是 $s$ 的前缀当且仅当从 $s$ 的末尾删去若干个（可以为 0 个）连续的字符后与 $t$ 相同。
		  
		  输入的字符串大小敏感。例如，字符串 `Fusu` 和字符串 `fusu` 不同。
		- ## 输入格式
		  
		  **本题单测试点内有多组测试数据**。  
		  
		  输入的第一行是一个整数，表示数据组数 $T$。
		  
		  对于每组数据，格式如下：  
		  第一行是两个整数，分别表示模式串的个数 $n$ 和询问的个数 $q$。  
		  接下来 $n$ 行，每行一个字符串，表示一个模式串。  
		  接下来 $q$ 行，每行一个字符串，表示一次询问。
		- ## 输出格式
		  
		  按照输入的顺序依次输出各测试数据的答案。  
		  对于每次询问，输出一行一个整数表示答案。
		- ## 输入输出样例 1
		- ### 输入 1
		  ```
		  3
		  3 3
		  fusufusu
		  fusu
		  anguei
		  fusu
		  anguei
		  kkksc
		  5 2
		  fusu
		  Fusu
		  AFakeFusu
		  afakefusu
		  fusuisnotfake
		  Fusu
		  fusu
		  1 1
		  998244353
		  9
		  ```
		- ### 输出 1
		  ```
		  2
		  1
		  0
		  1
		  2
		  1
		  ```
		- ## 说明/提示
		- ### 数据规模与约定
		  
		  对于全部的测试点，保证 $1 \leq T, n, q\leq 10^5$，且输入字符串的总长度不超过 $3 \times 10^6$。输入的字符串只含大小写字母和数字，且不含空串。
		- ### 说明
		  std 的 IO 使用的是关闭同步后的 cin/cout，本题不卡常。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=3e6+5;
		  int t[N][62],cnt[N],idx;
		  int tran(char x){
		  	if(x>='A'&&x<='Z') return x-'A';
		  	else if(x>='a'&&x<='z') return x-'a'+26;
		  	else return x-'0'+52;
		  }
		  void init(){
		  	for(int i=0;i<=idx;i++) cnt[i]=0;
		  	for(int i=0;i<=idx;i++)
		  		for(int j=0;j<=62;j++) t[i][j]=0;
		  	idx=0;
		  }
		  void insert(string s){
		  	int p=0;
		  	for(int i=0;s[i];i++){
		  		int x=tran(s[i]);
		  		if(!t[p][x]) t[p][x]=++idx;
		  		p=t[p][x];
		  		cnt[p]++;//模板题需要统计前缀数量故每次cnt[p]++
		  	}
		  }
		  int query(string s){
		  	int p=0;
		  	for(int i=0;s[i];i++){
		  		int x=tran(s[i]);
		  		if(!t[p][x]) return 0;
		  		p=t[p][x];
		  	}
		  	return cnt[p];
		  }
		  void solve(){
		  	init();
		  	int n,m;cin>>n>>m;
		  	string str;
		  	for(int i=1;i<=n;i++) cin>>str,insert(str);
		  	for(int i=1;i<=m;i++){
		  		cin>>str;
		  		cout<<query(str)<<endl;
		  	}
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	int t=1;cin>>t;
		  	while(t--) solve();
		  	return 0;
		  }
		  ```
- P2580 于是他错误的点名开始了
	- 题目
		- # P2580 于是他错误的点名开始了
		- ## 题目背景
		  XS中学化学竞赛组教练是一个酷爱炉石的人。
		  他会一边搓炉石一边点名以至于有一天他连续点到了某个同学两次，然后正好被路过的校长发现了然后就是一顿欧拉欧拉欧拉（详情请见已结束比赛 CON900）。
		- ## 题目描述
		  这之后校长任命你为特派探员，每天记录他的点名。校长会提供化学竞赛学生的人数和名单，而你需要告诉校长他有没有点错名。（为什么不直接不让他玩炉石。）
		- ## 输入格式
		  第一行一个整数 $n$，表示班上人数。
		  接下来 $n$ 行，每行一个字符串表示其名字（互不相同，且只含小写字母，长度不超过 $50$）。
		  第 $n+2$ 行一个整数 $m$，表示教练报的名字个数。
		  接下来 $m$ 行，每行一个字符串表示教练报的名字（只含小写字母，且长度不超过 $50$）。
		- ## 输出格式
		  对于每个教练报的名字，输出一行。
		  如果该名字正确且是第一次出现，输出 `OK`，如果该名字错误，输出 `WRONG`，如果该名字正确但不是第一次出现，输出 `REPEAT`。
		- ## 输入输出样例 1
		- ### 输入 1
		  ```
		  5  
		  a
		  b
		  c
		  ad
		  acd
		  3
		  a
		  a
		  e
		  ```
		- ### 输出 1
		  ```
		  OK
		  REPEAT
		  WRONG
		  ```
		- ## 说明/提示
		- 对于 $40\%$ 的数据，$n\le 1000$，$m\le 2000$。
		- 对于 $70\%$ 的数据，$n\le 10^4$，$m\le 2\times 10^4$。
		- 对于 $100\%$ 的数据，$n\le 10^4$，$m≤10^5$。
		  ---
		  $\text{upd 2022.7.30}$：新增加一组 Hack 数据。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define endl '\n'
		  const int N=1e5+5;
		  int n,m,t[N*51][26],idx;
		  bool cnt[N*51],vis[N*51];
		  string s;
		  int tran(char c){return c-'a';}
		  void insert(string s){
		  	int p=0;
		  	for(int i=0;s[i];i++){
		  		int x=tran(s[i]);
		  		if(!t[p][x]) t[p][x]=++idx;
		  		p=t[p][x];
		  	}
		  	cnt[p]=1;
		  }
		  int query(string s){
		  	int p=0;
		  	for(int i=0;s[i];i++){
		  		int x=tran(s[i]);
		  		if(!t[p][x]) return 0;
		  		p=t[p][x];
		  	}
		  	if(!cnt[p]) return 0;
		  	if(!vis[p]){
		  		vis[p]=1;
		  		return 1;
		  	}else return 2;
		  }
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		  	cin>>n;
		  	for(int i=1;i<=n;i++) cin>>s,insert(s);
		  	cin>>m;
		  	for(int i=1;i<=m;i++){
		  		cin>>s;
		  		int ret=query(s);
		  		if(ret==0) cout<<"WRONG"<<endl;
		  		else if(ret==1) cout<<"OK"<<endl;
		  		else cout<<"REPEAT"<<endl;
		  	}
		      return 0;
		  }
		  ```