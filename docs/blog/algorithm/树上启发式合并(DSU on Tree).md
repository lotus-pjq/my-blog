---
title: 树上启发式合并(DSU on Tree)
date: 2025-09-03
category: 图论
tags:
  - 算法
outline: deep
---

## 引入(OIwiki) :
- #### Q:启发式算法是什么呢？
- #### A:启发式算法是基于人类的经验和直观感觉，对一些算法的优化。
- 举个例子，最常见的就是**并查集的启发式合并**了，代码是这样的： 
	  ```
	  void merge(int x, int y) {
	    int xx = find(x), yy = find(y);
	    if (size[xx] 
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=1e5+10;
		  int n,col[N],siz[N],son[N],cnt[N],mx;
		  int sum,ans[N];
		  vectore[N];
		  void dfs1(int x,int fa){ 
		  	siz[x]=1;
		  	for(int y:e[x]){
		  		if(y==fa) continue;
		  		dfs1(y,x);
		  		siz[x]+=siz[y];
		  		if(siz[y]>siz[son[x]]) son[x]=y;
		  	}
		  }
		  void add(int x,int fa,int son){
		  	cnt[col[x]]++;
		  	if(cnt[col[x]]>mx) mx=cnt[col[x]],sum=col[x];
		  	else if(cnt[col[x]]==mx) sum+=col[x];
		  	for(int y:e[x]) //重子树除外
		  		if(y!=fa&&y!=son) add(y,x,son);
		  }
		  void sub(int x,int fa){//减去轻子树贡献
		  	cnt[col[x]]--;
		  	for(int y:e[x])
		  		if(y!=fa) sub(y,x);
		  }
		  void dfs2(int x,int fa,int opt){
		  	//opt:0->轻儿子,1->重儿子
		  	for(int y:e[x]) //先搜轻儿子，确定轻儿子的ans[x]
		  		if(y!=fa&&y!=son[x]) dfs2(y,x,0);
		  	if(son[x]) dfs2(son[x],x,1); //再搜重儿子
		  	add(x,fa,son[x]); //累计x和轻子树贡献
		  	ans[x]=sum;       
		  	if(!opt) sub(x,fa),sum=mx=0;//减去轻子树贡献并清空
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n;
		  	for(int i=1;i>col[i];
		  	for(int i=1,x,y;i>x>>y;
		  		e[x].push_back(y);
		  		e[y].push_back(x);
		  	}
		  	dfs1(1,0);
		  	dfs2(1,0,0);
		  	for(int i=1;i
		  using namespace std;
		  #define int long long
		  #define endl '\n'
		  const int N=2e5+10;
		  int n,col[N],siz[N],son[N],mx;
		  unordered_map cnt;
		  int ans[N],color,root;
		  int indgr[N];
		  vectore[N];
		  void dfs1(int x,int fa){ 
		  	siz[x]=1;
		  	for(int y:e[x]){
		  		if(y==fa) continue;
		  		dfs1(y,x);
		  		siz[x]+=siz[y];
		  		if(siz[y]>siz[son[x]]) son[x]=y;
		  	}
		  }
		  void add(int x,int fa,int son){
		  	cnt[col[x]]++;
		  	if(cnt[col[x]]>mx) mx=cnt[col[x]],color=col[x];
		  	else if(cnt[col[x]]==mx&&color>col[x]) color=col[x];
		  	for(int y:e[x]) //重子树除外
		  		if(y!=fa&&y!=son) add(y,x,son);
		  }
		  void sub(int x,int fa){//减去轻子树贡献
		  	cnt[col[x]]--;
		  	for(int y:e[x])
		  		if(y!=fa) sub(y,x);
		  }
		  void dfs2(int x,int fa,int opt){
		  	//opt:0->轻儿子,1->重儿子
		  	for(int y:e[x]) //先搜轻儿子，确定轻儿子的ans[x]
		  		if(y!=fa&&y!=son[x]) dfs2(y,x,0);
		  	if(son[x]) dfs2(son[x],x,1); //再搜重儿子
		  	add(x,fa,son[x]); //累计x和轻子树贡献
		  	ans[x]=color;       
		  	if(!opt) sub(x,fa),mx=0;//减去轻子树贡献并清空
		  }
		  signed main(){
		  	ios::sync_with_stdio(false);
		  	cin.tie(nullptr);
		  	cin>>n;
		  	for(int i=1;i>col[i];
		  	for(int i=1,x,y;i>x>>y;
		  		indgr[y]++;
		  		e[x].push_back(y);
		  		e[y].push_back(x);
		  	}
		  	for(int i=1;i<=n;i++)
		  		if(!indgr[i]){root=i;break;}
		  	dfs1(root,0);
		  	dfs2(root,0,0);
		  	for(int i=1;i<=n;i++) cout<<ans[i]<<" ";
		  	return 0;
		  }
		  ```