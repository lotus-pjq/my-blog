---
title: codeforces数论专项练习
date: 2025-10-20
category: 数论
tags:
  - 算法
outline: deep
---

### [2148G - Farmer John's Last Wish](https://codeforces.com/problemset/problem/2148/G) #1900 #数论 #前缀 #gcd #筛法 #因数- 题目- 
- 思路- 
  - 
- 代码

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  int a[N],cnt[N];
		  bool vis[N];
		  vector divs[N];
		  void sieve(int n){
		      for(int i=2;i>n;
		  	vector cur;//cur:（目前）前i个数的公因子集合
		  	for(int i=0;i>a[i];
		  	int ans=0;
		  	for(int i=1;i nxt;
		  		for(int x:divs[a[i]]){
		  			cnt[x]++;
		  			if(cnt[x]!=i) ans=max(ans,cnt[x]);
		  			else if(!vis[x]){
		  				nxt.push_back(x);
		  				vis[x]=1;
		  			}
		  		}
		  		for(int x:cur){
		  			if(cnt[x]!=i){
		  				ans=max(ans,cnt[x]);
		  				vis[x]=0;
		  			}else nxt.push_back(x);
		  		}
		  		cur=nxt;
		  		cout>t;
		      while(t--) solve();
		      return 0;
		  }
		  ```
- ### [2123G - Modular Sorting](https://codeforces.com/problemset/problem/2123/G) #数论 #离线 #因数 #筛法- 题目- 
  - 
  - 
- 思路（芋饼饭）- [G_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1FT34zXE1w?spm_id_from=333.788.videopod.sections&vd_source=f5831e237a3085475240ade264213933&p=7)
- *代码

```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=5e5+5;
		  int n,m,op,x,y;
		  int a[N],q[N][3],b[N],res[N];
		  int gcd(int a,int b){
		  	int tmp;
		  	while(b!=0){tmp=a%b;a=b;b=tmp;}
		  	return a;
		  }
		  vector fac[N];
		  void sieve(){
		  	for(int i=1;i>n>>m>>qn;
		  	for(int i=1;i>a[i];
		  	for(int i=1;i>q[i][0];
		  		if(q[i][0]==1) cin>>q[i][1]>>q[i][2];
		  		else cin>>q[i][1];
		  	}
		  	for(int i=1;ib[i+1]) sum++;
		  		for(int i=1;i=1&&b[pos-1]>b[pos]) sum--;
		  				if(pos+1b[pos+1]) sum--;
		  				b[pos]=q[i][2]%d;
		  				if(pos-1>=1&&b[pos-1]>b[pos]) sum++;
		  				if(pos+1b[pos+1]) sum++;
		  			}else if(gcd(q[i][1],m)==d) res[i]=(sum>t;
		      while(t--) solve();
		      return 0;
		  }
		  
		  ```
- 思路1（题解）- 
  - 
- 代码1（题解）

```C++
		  #include 
		  using namespace std;
		  int mod(int a, int m){return (a % m + m) % m;}
		  void solve(){
		      int n, m, q, op, i, x, k;
		      cin >> n >> m >> q;
		      vector a(n+1);
		      for(int i=1; i> a[i];
		      map ans;
		      for(int i=1; i*i p : ans)
		          for(int i=1; i> op;
		          if(op == 1){
		              cin >> i >> x;
		              for(pair p : ans){
		                  ans[p.first] += mod(x - a[i-1], p.first) - mod(a[i] - a[i-1], p.first);
		                  if(i != n)
		                      ans[p.first] += mod(a[i+1] - x, p.first) - mod(a[i+1] - a[i], p.first);
		              }
		              a[i] = x;
		          }
		          else{
		              cin >> k;
		              cout > t;
		      while(t--) solve();
		  }
		  ```
- 思路2（题解）- 
		-
- 代码2（题解）

```C++
		  #include 
		  using namespace std;
		  void solve(){
		      int n, m, q, op, i, x, k;
		      cin >> n >> m >> q;
		      vector a(n+1);
		      for(int i=1; i> a[i];
		      map ans;
		      for(int i=1; i*i p : ans)
		          for(int i=1; i> op;
		          if(op == 1){
		              cin >> i >> x;
		              for(pair p : ans){
		                  ans[p.first] += (x % p.first > k;
		              cout > t;
		      while(t--) solve();
		  }
		  ```
- ### 2118D2 - Red Light, Green Light (Hard version)- 题目- 
  - 
  - INPUT- 4
			  2 2
			  1 4
			  1 0
			  3
			  1 2 3
			  9 4
			  1 2 3 4 5 6 7 8 9
			  3 2 1 0 1 3 3 1 1
			  5
			  2 5 6 7 8
			  4 2
			  1 2 3 4
			  0 0 0 0
			  4
			  1 2 3 4
			  3 4
			  1 2 3
			  3 1 1
			  3
			  1 2 3
  - OUTPUT- YES
			  NO
			  YES
			  YES
			  YES
			  YES
			  NO
			  NO
			  YES
			  YES
			  NO
			  NO
			  YES
			  NO
			  YES
- 思路（？
- 代码
  - ```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  #define INF 0x3f3f3f3f3f3f3f3f
		  const int N=2e5+5;
		  int p[N],delay[N],d[Nx.pos;}
		  }q[N];
		  bool dfs(int x){
		  	if(x==-1) return true;
		  	if(vis[x]) return ext[x];
		  	vis[x]=true;
		  	ext[x]=dfs(d[x]);
		  	return ext[x];
		  }
		  void solve(){
		  	int n,k;cin>>n>>k;
		  	for(int i=1;i>p[i];
		  	for(int i=1;i>delay[i];
		  	int qn;cin>>qn;
		  	for(int i=1;i>q[i].pos,q[i].id=i;
		  	sort(q+1,q+qn+1);
		  	//1...n: 红灯的时候往右边走
		  	//n+1...2n:红灯的时候往左边走
		  	for(int i=1;i idx;
		  	for(int i=n;i>=1;i--){
		  		if(idx.count(a[i])) d[i]=idx[a[i]]+n;
		  		idx[a[i]]=i;
		  	}
		  	for(int i=1;i=0&&p[ai]>=q[i].pos){
		  			idx[a[ai]]=ai;
		  			ai--;
		  		}
		  		if(!idx.count(q[i].pos%k)) res[q[i].id]=true;
		  		else res[q[i].id]=ext[idx[q[i].pos%k]+n];
		  	}
		  	for(int i=1;i>t;
		      while(t--) solve();
		      return 0;
		  }
		  ```
- ### 2154C2 - No Cost Too Great (Hard Version) #数学 #筛法 #gcd #质因数- 题目- 
  - 
- 分析- 
- 代码

```C++
		  #include
		  using namespace std;
		  #define fi first
		  #define se second
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+5;
		  struct node{
		  	int a,b;
		  	bool operator mpf;
		  void sieve(int n){
		  	mpf.resize(n+1,0);
		  	for(int i=2;i st;
		  	cin>>n;
		  	for(int i=1;i>x[i].a;
		  	for(int i=1;i>x[i].b;
		  	sort(x+1,x+n+1);
		  	for(int i=1;i tmp;
		  		while(cur>1){
		  			int p=mpf[cur];
		  			if(st.count(p)){cout1){
		  			int p=mpf[cur];
		  			if(st.count(p)){ans=min(ans,x[i].b);break;}
		  			while(cur%p==0) cur/=p;
		  		}
		  	}
		  	int cnt=2e9;//不能太大，不然下面cnt*x[1].b会爆longlong
		  	for(int i=2;i1){
		  			int p=mpf[cur];
		  			cnt=min(cnt,p-x[1].a%p);
		  			while(cur%p==0) cur/=p;
		  		}
		  	}
		  	ans=min(ans,cnt*x[1].b);
		  	cout>t;
		  	while(t--) solve();
		  	return 0;
		  }
		  ```
-