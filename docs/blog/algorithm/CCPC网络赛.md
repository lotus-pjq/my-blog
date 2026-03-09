---
title: CCPC网络赛
date: 2025-09-22
category: 博弈论
tags:
  - 算法
outline: deep
---

- 榜单地址：https://pintia.cn/rankings/1967841176776331264
- 竞赛地址：https://qoj.ac/contest/2534
- ---
- ### F.连线博弈 #博弈论 #异或哈希
- 题面：
  - 
- 分析：
  - > Tip1:要注意要看成始终"环"的状态，不存在线的状态。
		  > Tip2:就算点不相邻也可能会在同一个"环"中、
  - 
  - 为找到初始棋盘的子游戏大小，考虑 Xor-Hash，即对圆环 Hash 染色，颜色（即异或值）相同的在一个子游戏中。
  - 博弈部分是模板题：sg 打表，同一状态下的子游戏 - 异或；同一游戏后续的子状态 - mex。
		  打表发现规律：34个一组循环，其中前两组有部分点不符合后续循环规律
		  
- 代码：
  - ```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e2+5;
		  mt19937_64 rg(random_device{}());
		  int sg[N];
		  int SG(int x){
		  	if(x st;
		  	for(int i=0;i>n>>m;
		  	pair pr[2*m+5];
		  	int tot=0;
		  	for(int i=1,l,r;i>l>>r;
		  		int rnd=rg();
		  		pr[++tot]={l,rnd},pr[++tot]={r,rnd};
		  	}
		  	sort(pr+1,pr+tot+1);
		  	pr[++tot]={n,0};
		  	map seg;
		  	int lst=-1,cur=0;
		  	for(int i=1,x,val;i>t;
		  	while(t--) solve();
		  	return 0;
		  }
		  ```
  - 
- ### G.序列与整数对 #分块
- 题面：- 
- 法一（O(q*logn*√n)）- 
  - ```C++
		  #include
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	int n,q,x,B;cin>>n>>q;
		  	B=500;
		  	map> mp;
		  	for(int i=1;i>x;
		  		mp[x].push_back(i);
		  	}
		  	map,int> ans;
		  	while(q--){
		  		int x,y;cin>>x>>y;
		  		if(x==y){
		  			int siz=mp[x].size();
		  			cout vecx=mp[x],vecy=mp[y];
		  		if(vecx.size()B) ans[{x,y}]=res;
		  		cout<<res<<endl;
		  	}
		   	return 0;
		  }
		  ```
- 法二
		-