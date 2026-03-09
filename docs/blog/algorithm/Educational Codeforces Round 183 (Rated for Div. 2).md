---
title: Educational Codeforces Round 183 (Rated for Div. 2)
date: 2025-10-07
category: 题解
tags:
  - 算法
outline: deep
---

### B
- 代码

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  int n,m,a[N];
		  void solve(){
		  	int n,k;cin>>n>>k;
		  	string s;cin>>s;
		  	int a,b,m;a=b=m=0;
		  	for(char c:s){
		  		if(c=='0') a++;
		  		else if(c=='1') b++;
		  		else m++;
		  	}
		  	for(int i=0;ir)||(l>0);
		  		bool you=(l=0);
		  		if(wu&&you) cout>t;
		  	while(t--)solve();
		  	return 0;
		  }
		  ```
- ### C #字符串- 代码
  - ```C++
		  #include
		  using namespace std;
		  #define endl '\n'
		  #define INF 0x3f3f3f3f3f3f3f3f
		  #define rep(i,j,k) for (int i=j;i>n;
		  	string s;cin>>s;s=" "+s;
		  	rep(i,0,4*n) a[i]=vis[i]=0;
		  	int ans=INF;
		  	int cha=0;
		  	rep(i,1,n){
		  		if(s[i]=='a') cha++;
		  		else cha--;
		  	}
		  	int cnt=0;
		  	vis[2*n]=1;a[2*n]=0;
		  	rep(i,1,n){
		  		if(s[i]=='a') cnt++;
		  		else cnt--;
		  		if(vis[cnt+2*n-cha]) ans=min(ans,i-a[cnt+2*n-cha]);
		  		vis[cnt+2*n]=1;
		  		a[cnt+2*n]=i;
		  	}
		  	if(cha==0) cout>t;
		      while(t--) solve();
		      return 0;
		  }v
		  ```
- ### D #dfs #回溯 #剪枝
- 代码

```C++
		  #include
		  using namespace std;
		  #define endl '\n'
		  const int N=2e5+5;
		  int tot;
		  int cur[N];
		  bool f;
		  int pos,cnt,n,k;
		  int ans[N];
		  void out(){
		  	int p=0,q=0,num=n;
		  	for(int i=cnt+1;ip;i--) ans[i]=num--;
		  		p+=cur[i];
		  	}
		  	for(int i=1;in) return;
		  	if(res==0){f=1;out();return;} 
		  	int tmp=sqrt(2*res);
		  	for(int i=tmp+1;i>=max(tmp-1,2);i--){
		  		if(res>=i*(i-1)/2){
		  			cur[++pos]=i;
		  			cnt+=i;
		  			dfs(res-i*(i-1)/2);
		  			pos--;
		  			cnt-=i;
		  		}
		  	}
		  }
		  void solve(){
		  	cin>>n>>k;
		  	f=false;
		  	pos=cnt=0;
		  	dfs(n*(n-1)/2-k);
		  	if(!f) cout>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```