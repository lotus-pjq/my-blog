---
title: 2020-2021 Winter Petrozavodsk Camp, Belarusian SU Contest (XXI Open Cup, Grand Prix of Belarus)题解
date: 2026-03-09
category: 题解
tags:
  - 算法
description: 2020-2021 Winter Petrozavodsk Camp, Belarusian SU Contest (XXI Open Cup, Grand Prix of Belarus)题解相关的算法笔记和代码模板
---

- 网站：https://codeforces.com/gym/102956
- ### C. Brave Seekers of Unicorns #DP #按位
	- 题意
		- 定义一个好序列满足如下条件：
			- 序列非空。
			- 没有三个连续的元素异或和为0。
			- 序列递增。
			- 序列的值域为$[1,n]$。
		- 给定 $n$ ,对好序列计数，答案对998244353取模。
	- 思路
		- 考虑dp: dp[i]表示以i结尾的合法序列的个数: $$ dp[i] = \sum_{j=1}^{i-1} dp[j] - [j \oplus i < j] *  dp[{j\oplus i}] $$
		- 维护dp[]的前缀和数组pre[]:  $$ pre[i]=\sum_{j=1}^{i}dp[j] $$
		- 因为要考虑 \(i \oplus j \oplus k = 0\) 的情况，所以一个位上最多只有两个 1。
		- 枚举二进制上 \(i\) 的除最高位的 1 位 \(d\)，钦定 \(j\) 的第 \(d\) 位是 1，\(k\) 的第 \(d\) 位为 0，那么第 \(d\) 位往后都可以随便乱取。
		  那么 \(k\) 的范围就是 \([2^d, 2^{d+1} - 1]\)。
		- 时间复杂度 \(O(n \log n)\)。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  #define per(i,j,k) for (int i=j;i>=k;--i)
		  const int mod=998244353;
		  const int N=1e6+5;
		  int n;
		  int dp[N];
		  int pre[N];
		  //dp[i]:以i结尾的合法序列的个数
		  //pre[i]=sigema{j=1->i}dp[j]
		  //dp[i]:(pre[i-1]+1)-sigema{j=1->i-1}[(i^j)<j]*dp[i^j];
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		  	cin>>n;
		  	pre[1]=dp[1]=1;
		  	rep(i,2,n){
		  		dp[i]=(pre[i-1]+1)%mod;
		  		int p;
		  		for(p=20;p>=0;p--)
		  			if(i>>p&1) break;
		  		int mns=0;
		  		per(j,p-1,0){
		  			if(i>>j&1) mns=(mns+(pre[(1<<(j+1))-1]-pre[(1<<j)-1])%mod+mod)%mod;
		  		}
		  		dp[i]=((dp[i]-mns)%mod+mod)%mod;
		  		pre[i]=(pre[i-1]+dp[i])%mod;
		  	}
		  	cout<<pre[n];
		      return 0;
		  }
		  ```
- ### D. Bank Security Unification #DP #按位
	- 题意
		- 从一个长度为 \(n\) 的序列中找出一个子序列，使得相邻元素的按位与值的和最大。
		- 其中 $$2<=n<=10^6 , 0<=a_i<=10^{12} $$
	- 思路
		- 我们利用dp和二进制位的特性优化问题。
		- 考虑$$dp[i]$$:以$$i$$为结尾的子序列的值最大是多少。
		- 由于按位与的和是“单调”的，考虑遍历到当前的某一位，贪心的选择越靠后的进行转移更加优秀 （可以视作对暴力dp的剪枝） 。
		- 所以考虑用数组 $$las[j][0/1] $$表示遍历到当前的第i个数的第j位从哪里上一个哪个下标转移来。
		- 时间复杂度为 \(O(n \log a_i)\)。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i<=k;++i)
		  const int N=1e6+5;
		  int n,a[N],ans;
		  int las[41][2];
		  int dp[N];
		  //las[j][0/1]:第j位上的0/1
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		  	cin>>n;
		  	rep(i,1,n) cin>>a[i];
		  	rep(j,0,40){
		  		if(a[1]>>j&1) las[j][1]=1;
		  		else las[j][0]=1;
		  	}
		  	rep(i,2,n){
		  		rep(j,0,40){
		  			int bm=a[i]>>j&1;
		  			dp[i]=max(dp[i],dp[las[j][bm]]+(a[las[j][bm]]&a[i]) );
		  		}
		  		ans=max(ans,dp[i]);
		  		rep(j,0,40){
		  			if(a[i]>>j&1) las[j][1]=i;
		  			else las[j][0]=i;
		  		}
		  	}
		  	cout<<ans;
		      return 0;
		  }
		  ```
- ### G. Biological Software Utilities #计数 #树
	- 题意
		- 求存在完美匹配的n个点的树的数量，对998244353取模。
		- 完美匹配：对一颗树进行删边后，存在使所得到的图仅由2个顶点的连通分量组成。
		- 其中 $$1<=n<=10^6$$
	- 思路
		- 因为最后肯定是两两匹配，我们先考虑分组，再考虑连边成树。
		- 分组：选出 $n/2$ 对组合的数量是$sum=(n-1)*(n-3)*....*3*1$。
		- 连边成树：已知给定n个不同的点，组成的无根树的个数有$n^{n-2}$。
		- 对于2对组合之间的连边有4种可能
		- 所以$ans=ksm(n/2,n/2-2)*ksm(4,n/2-1)*sum$
		- 注意取模。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int mod=998244353;
		  int ksm(int x,int y){
		  	int ans=1;
		  	while(y){
		  		if(y&1)ans=ans*x%mod;
		  		x=x*x%mod;y>>=1;
		  	}return ans;
		  }
		  signed main(){
		      ios::sync_with_stdio(0);
		      cin.tie(0);cout.tie(0);
		  	int n;cin>>n;
		  	if(n%2==1) cout<<0<<endl;
		  	else if(n==2) cout<<1<<endl;
		  	else{
		  		int sum=ksm(n/2,n/2-2)*ksm(4,n/2-1)%mod;
		  		int h=(n-1);
		  		while(h>=1){
		  			sum=(sum*h)%mod;
		  			h-=2;
		  		}
		  		cout<<sum<<endl;
		  	}
		  }
		  ```
- ### I. Binary Supersonic Utahraptors #game
	- 题意
		- Alice 和 Bob 又在玩游戏，Alice 有黑与白两种物品，Bob 也有黑与白两种物品。
		- 有 $$k$$ 个回合，每一回合中，Alice 先送给 Bob  $$S_i $$ 个物品，Bob 则回礼 $$S_i$$ 个物品。
		- Alice 想让 Alice 的黑物品与 Bob 的白物品差尽可能小，Bob 则想让上述东西最大。
		- 求最后的这个值。
		- 其中 $$1<=n,m,k<=3*10^5$$ 。
	- 思路
		- Alice 和 Bob 并不能决定这一切。
		  答案是总的黑物品数与 $$n$$ 的差。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  signed main(){
		      ios::sync_with_stdio(false);
		      cin.tie(nullptr);
		  	int n,m,k;cin>>n>>m>>k;
		  	int y0=0,tmp;
		  	rep(i,1,n){
		  		cin>>tmp;
		  		if(!tmp) y0++;
		  	}
		  	int y1=0;
		  	rep(i,1,m){
		  		cin>>tmp;
		  		if(!tmp) y1++;
		  	}
		  	rep(i,1,k) cin>>tmp;
		  	int tot=y0+y1;
		  	cout<<abs(tot-m)<<endl;
		      return 0;
		  }
		  ```
- ### J. Burnished Security Updates #dfs #二分图
	- 题意
		- 求一张n个点m条边的图的最小覆盖所有边的顶点集大小。
		- 其中 $$2<=n<=3*10^5 , 1<=m<=3*10^5$$。
	- 思路
		- 要覆盖所有边，所以相邻的两个点一定取得状态不同。
		  考虑二分图染色，如果原图有奇环，则一定无解，否则取较小的那种颜色的点集。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define pb push_back
		  const int N=3e5+5;
		  int n,m,col[N],cnt[2],ans;
		  vector<int> e[N];
		  bool dfs(int u,int c) {
		      col[u]=c, cnt[c]++;
		  	c^=1;
		      bool f=1;
		      for(auto v:e[u])
		          if(col[v]==-1) f&=dfs(v,c);
		          else if(col[v]==col[u]) return 0;
		      return 1;
		  }
		  signed main() {
		      cin>>n>>m;
		      for(int i=1,u,v;i<=m;i++) {
		          cin>>u>>v;
		          e[u].pb(v);
		  		e[v].pb(u);
		      }
		  	for(int i=1;i<=n;i++) col[i]=-1;
		      for(int i=1;i<=n;i++)
		          if(col[i]==-1){
		              cnt[1]=cnt[0]=0;
		              if(!dfs(i,1)) {
		                  cout<<-1<<endl;
		                  return 0;
		              }
		              ans+=min(cnt[1],cnt[0]);
		          }
		  	cout<<ans<<endl;
		  }
		  ```
- ###  M. Brilliant Sequence of Umbrellas #构造 #gcd
	- 题意
		- 构造一个长度至少为 \(\lceil\frac{2}{3}\sqrt{n}\rceil\) 的值域为 \([1, n]\) 的递增序列，使得两两之间的 \(\text{gcd}\) 也递增。
	- 思路
		- 一开始看到√n,很自然想到构造{i*(i+1)}来试图让相邻两数gcd为$$i$$,但是一下子没想到 $$i-1$$ 和 $$i+1$$ 会对gcd有贡献。
		- （当时很疑惑为什么是\(\lceil\frac{2}{3}\sqrt{n}\rceil\)，这个2/3也有什么意义？）
		- 那只需要将数组构造成$$num[i]*num[i+1]$$，并且保证$$num[i]$$与$$num[i+2]$$互质即可，则 $$ gcd(num[i-1]*num[i]$$ $$, num[i]*num[i+1])=num[i] $$
		- 观察样例，考虑构造一个每隔两个数均互质的序列，然后将这个序列相邻两项的积作为原序列。这样一定满足 \(\text{gcd}\) 递增。
	- 代码
		- ```C++
		  #include<bits/stdc++.h>
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=1e6+5;
		  int a[N];
		  int gcd(int a,int b){
		  	int tmp;
		  	while(b!=0){tmp=a%b;a=b;b=tmp;}
		  	return a;
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	int p=0;
		  	int n;cin>>n;
		  	int w=ceil(2.0*sqrtl(n)/3);
		  	a[0]=1, a[++p]=1;
		  	int last=1;
		  	for(int i=2;p<=w;i++)
		  		if(gcd(a[p-1],i)==1) a[++p]=i;
		  	cout<<p-1<<endl;
		  	for(int i=1;i<p;i++) cout<<a[i]*a[i-1]<<" ";
		  	cout<<endl;
		  	return 0;
		  }
		  ```