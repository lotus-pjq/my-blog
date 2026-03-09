---
title: Codeforces Round 1056 (Div. 2)
date: 2025-10-06
category: 题解
tags:
  - 算法
outline: deep
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

```C++
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
		  cout UUUUUU
		  UUUDDD
		   RRRRRR
		   RRRRRL
- 代码

```C++
		  #include
		  using namespace std;
		  #define endl '\n'
		  const int N=1e5+5;
		  int n,k;
		  char mp[N];
		  void solve(){
		  	cin>>n>>k;
		  	if(k==n*n-1){cout>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```
- ### C #模拟
- 题意
  - 有 `n` 个巫师从左到右排成一行，编号从 `1` 到 `n`。每个巫师的隐形斗篷可以穿在左侧或右侧。Harry 从巫师 `1` 的位置走到巫师 `n` 的位置，并在每个巫师 `i` 的位置记录他看到的巫师数量。从位置 `i` 可以看到巫师 `j` 的条件是：
  - 如果巫师 `j` 的斗篷穿在左侧（即向左覆盖），则必须满足 `i >= j`（即 Harry 在 `j` 的右侧或同一位置）。
  - 如果巫师 `j` 的斗篷穿在右侧（即向右覆盖），则必须满足 `i  (... (...>>...)$
  - $a[i+1]=a[i]-1   (...<>...)或(...><>...<>：n/2+1$
  - 2、$n$ 为偶数时
			  $<><>...<>：n/2+1$
			  $><>)$，然后验证$a[i]==pre[i]+suf[i]$
- 代码

```C++
		  #include
		  using namespace std;
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i=k;--i)
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
		  			if(a[1]==n/2+1||a[1]==n/2) cout0&&b[p]==0){
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
		  	if(!flag) cout>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```