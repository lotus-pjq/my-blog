---
title: 2020-2021 Winter Petrozavodsk Camp, Belarusian SU Contest (XXI Open Cup, Grand Prix of Belarus)题解
date: 2025-10-05
category: 题解
tags:
  - 算法
outline: deep
---

- 网站：https://codeforces.com/gym/102956
- ### C. Brave Seekers of Unicorns #DP #按位
- 题意- 定义一个好序列满足如下条件：
  - 序列非空。
  - 没有三个连续的元素异或和为0。
  - 序列递增。
  - 序列的值域为$[1,n]$。
  - 给定 $n$ ,对好序列计数，答案对998244353取模。
- 思路
  - 考虑dp: dp[i]表示以i结尾的合法序列的个数: $$ dp[i] = \sum_{j=1}^{i-1} dp[j] - [j \oplus i 
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i=k;--i)
		  const int mod=998244353;
		  const int N=1e6+5;
		  int n;
		  int dp[N];
		  int pre[N];
		  //dp[i]:以i结尾的合法序列的个数
		  //pre[i]=sigema{j=1->i}dp[j]
		  //dp[i]:(pre[i-1]+1)-sigema{j=1->i-1}[(i^j)>n;
		  	pre[1]=dp[1]=1;
		  	rep(i,2,n){
		  		dp[i]=(pre[i-1]+1)%mod;
		  		int p;
		  		for(p=20;p>=0;p--)
		  			if(i>>p&1) break;
		  		int mns=0;
		  		per(j,p-1,0){
		  			if(i>>j&1) mns=(mns+(pre[(1
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define rep(i,j,k) for (int i=j;i>n;
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
		  	cout
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
		  	if(n%2==1) cout=1){
		  			sum=(sum*h)%mod;
		  			h-=2;
		  		}
		  		cout
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
		  	cout
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define pb push_back
		  const int N=3e5+5;
		  int n,m,col[N],cnt[2],ans;
		  vector e[N];
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
		      for(int i=1,u,v;i>u>>v;
		          e[u].pb(v);
		  		e[v].pb(u);
		      }
		  	for(int i=1;i
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