---
title: Codeforces Round 1056 (Div. 2)
date: 2026-03-09
category: 题解
tags:
  - 算法
description: Codeforces Round 1056 (Div. 2)相关的算法笔记和代码模板
---

### A #数学 #模拟
	- 题意
		- 题目要求计算在双败淘汰赛中总共进行的比赛场数，其中比赛过程包括胜者组和败者组的阶段，直到最终两队决出冠军。
	- 分析
		- 通过分析比赛机制，可以得出无论比赛过程如何，总比赛场数遵循固定公式：**总场次 = 2 × n - 2**。
		- ### 公式推导简要说明：
		- 每场比赛恰好产生一个失败者。
		- **胜者组比赛场次**：初始有 `n` 队，最终胜者组冠军只剩1队，因此需要进行 `n - 1` 场比赛（每场比赛减少1队）。
		- **败者组比赛场次**：在败者组中被淘汰的队伍总数为 `n - 1`（每场比赛淘汰1队），因此败者组共 `n - 1` 场比赛（包括决赛）。
		- **总场次**：胜者组场次加上败者组场次，即 $(n - 1) + (n - 1) = 2n - 2$。
		  因此，对于每个测试用例，直接输出 $2 * n - 2$ 即可。
	- 代码1（数学）：略
	- 代码2（模拟）
		- ```C++
		  int n;cin>>n;
		  int w=n;
		  int ans=0;
		  while(n>1){
		    ans+=n/2;
		    n-=n/2;
		  }
		  n=w-1;
		  while(n>1){
		    ans+=n/2;
		    n-=n/2;
		  }
		  ans+=1;
		  cout<<ans<<endl;
		  ```
- ### B #构造
	- 题意
		- 有 `t` 个测试用例。每个测试用例给定两个整数 `n` 和 `k`，要求为 `n × n` 网格的每个格子分配方向箭头（上 U, 下 D, 左 L, 右 R），使得：
		- 从某个格子出发时，会沿着箭头方向移动（每次移动1格）
		- 如果能移动到网格外，则该起始格子被视为"可逃脱"
		- 整个网格中**恰好有 `k` 个起始格子能让亚伯拉罕逃脱**
		- 需要在可行时输出任意满足条件的网格方案，否则输出 `NO`。
	- 分析
		- 前k个往上
		- 后面死循环就行
		- 形如:
		- > UUUUUU
		  UUUDDD
		   RRRRRR
		   RRRRRL
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define endl '\n'
		  const int N=1e5+5;
		  int n,k;
		  char mp[N];
		  void solve(){
		  	cin>>n>>k;
		  	if(k==n*n-1){cout<<"NO"<<endl;return;}
		  	cout<<"YES"<<endl;
		  	for(int i=1;i<=n*n;i++) mp[i]='R';
		  	for(int i=n;i<n*n;i+=n) mp[i]='D';
		  	mp[n*n]='L';
		  	for(int i=1;i<=k;i++)
		  		mp[i]='U';
		  	for(int i=1;i<=n*n;i++){
		  		cout<<mp[i];
		  		if(i%n==0) cout<<endl;
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
- ### C #模拟
	- 题意
		- 有 `n` 个巫师从左到右排成一行，编号从 `1` 到 `n`。每个巫师的隐形斗篷可以穿在左侧或右侧。Harry 从巫师 `1` 的位置走到巫师 `n` 的位置，并在每个巫师 `i` 的位置记录他看到的巫师数量。从位置 `i` 可以看到巫师 `j` 的条件是：
		- 如果巫师 `j` 的斗篷穿在左侧（即向左覆盖），则必须满足 `i >= j`（即 Harry 在 `j` 的右侧或同一位置）。
		- 如果巫师 `j` 的斗篷穿在右侧（即向右覆盖），则必须满足 `i <= j`（即 Harry 在 `j` 的左侧或同一位置）。
		- 注意：无论斗篷方向如何，从位置 `i` 总能看到巫师 `i`。
		- Harry 记录了一个长度为 `n` 的数组 `a`，其中 `a[i]` 表示从位置 `i` 看到的巫师数量。
		- 你的任务是计算有多少种斗篷方向安排方案（每个巫师的斗篷要么向左，要么向右），使得在每个位置 `i` 看到的巫师数量恰好等于 `a[i]`，并对 `676767677` 取模。
	- 分析
		- 关键在于分析相邻两项变化来确定唯一可能性：
			- 设第$i$为可见数量$a[i]$为$x$,
			- $a[i+1]=a[i]+1  <=> (...<<...)$
			- $a[i+1]=a[i]-1  <=> (...>>...)$
			- $a[i+1]=a[i]-1  <=> (...<>...)或(...><...)$
			- 只要存在$a[i]!=a[i+1]$那序列就可以唯一确定
		- 特殊情况：$a[i]$全相等时，
			- 1、 $n$为奇数时，
			  $<><>...<：n/2+1$
			  $><><...>：n/2+1$
			- 2、$n$ 为偶数时
			  $<><>...<>：n/2+1$
			  $><><..><：n/2$
		- 只需要确定唯一可能序列后验证$a[i]$是否符合，考虑记录前后缀：$pre(<)$和$suf(>)$，然后验证$a[i]==pre[i]+suf[i]$
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  #define per(i,j,k) for (int i=j;i>=k;--i)
		  const int N=2e5+5;
		  int n,a[N],b[N],pre[N],suf[N];
		  void solve(){
		  	cin>>n;
		  	bool f=true;
		  	rep(i,1,n) cin>>a[i];
		  	rep(i,1,n-1) 
		  		if(a[i+1]!=a[i]) f=false;
		  	if(f){
		  		if(n%2==0){
		  			if(a[1]==n/2+1||a[1]==n/2) cout<<1<<endl;
		  			else cout<<0<<endl;
		  		}else{
		  			if(a[1]==n/2+1) cout<<2<<endl;
		  			else cout<<0<<endl;
		  		}
		  		return;
		  	}
		  	rep(i,1,n) b[i]=0;
		  	bool flag=1;
		  	rep(i,1,n-1){
		  		if(a[i]==a[i+1]){
		  			if(b[i]) b[i+1]=-b[i];
		  		}else if(a[i+1]==a[i]+1){
		  			if(b[i]==1){flag=0;break;}
		  			b[i+1]=-1;
		  			if(b[i]==0){
		  				b[i]=-1;
		  				int p=i-1;
		  				while(p>0&&b[p]==0){
		  					b[p]=-b[p+1];
		  					p--;
		  				}
		  			}
		  		}else if(a[i+1]==a[i]-1){
		  			if(b[i]==-1){flag=0;break;}
		  			b[i+1]=1;
		  			if(b[i]==0){
		  				b[i]=1;
		  				int p=i-1;
		  				while(p>0&&b[p]==0){
		  					b[p]=-b[p+1];
		  					p--;
		  				}
		  			}
		  		}
		  	}
		  	if(!flag) cout<<0<<endl;
		  	else{ 
		  		// cout<<"TEST"<<endl;
		  		// rep(i,1,n) cout<<b[i]<<" ";
		  		// cout<<endl;
		  		suf[n+1]=0;
		  		rep(i,1,n){
		  			if(b[i]==-1) pre[i]=pre[i-1]+1;
		  			else pre[i]=pre[i-1];
		  		}
		  		per(i,n,1){
		  			if(b[i]==1) suf[i]=suf[i+1]+1;
		  			else suf[i]=suf[i+1];
		  		}
		  		int ans=1;
		  		rep(i,1,n)
		  			if(a[i]!=suf[i]+pre[i]){ans=0;break;}
		  		cout<<ans<<endl;
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