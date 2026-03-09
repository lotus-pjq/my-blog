---
title: Splay树
date: 2026-03-09
category: 数据结构
tags:
  - 算法
description: Splay树相关的算法笔记和代码模板
---

- #数据结构
- 无注释模版:
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  #define INF 0x3f3f3f3f3f3f3f3f
	  #define rep(i,j,k) for (int i=j;i<=k;++i)
	  #define per(i,j,k) for (int i=j;i>=k;--i)
	  const int mod=1e9+7;
	  const int N=2e5+5;
	  #define ls(x) tr[x].s[0]
	  #define rs(x) tr[x].s[1]
	  struct node{
	  	int s[2],fa,val,cnt,siz;
	  //左右儿,父,点权,个数,子树大小
	  	void init(int p,int v){
	  		fa=p, val=v;
	  		cnt=siz=1;
	  	}
	  }tr[N];
	  int root,tot;//根,节点数
	  void pushup(int x){tr[x].siz=tr[ls(x)].siz+tr[rs(x)].siz+tr[x].cnt;}
	  void rotate(int x){
	  	int y=tr[x].fa, z=tr[y].fa;
	  	int k=(tr[y].s[1]==x);
	  	tr[y].s[k]=tr[x].s[k^1];//1
	  	tr[tr[x].s[k^1]].fa=y;
	  	tr[x].s[k^1]=y;//2
	  	tr[y].fa=x;
	  	tr[z].s[tr[z].s[1]==y]=x;//3
	  	tr[x].fa=z;
	  	pushup(y),pushup(x);
	  }
	  void splay(int x,int k){
	  	while(tr[x].fa!=k){
	  		int y=tr[x].fa, z=tr[y].fa;
	  		if(z!=k) (ls(y)==x)^(ls(z)==y)?rotate(x):rotate(y);
	  		rotate(x);
	  	}
	  	if(!k) root=x;
	  }
	  void find(int v){
	  	int x=root;
	  	while(tr[x].s[v>tr[x].val]&&v!=tr[x].val)
	  		x=tr[x].s[v>tr[x].val];
	  	splay(x,0);
	  }
	  void insert(int v){
	  	int x=root, p=0;
	  	while(x&&tr[x].val!=v) p=x,x=tr[x].s[v>tr[x].val];
	  	if(x) tr[x].cnt++;
	  	else{
	  		x=++tot;
	  		tr[p].s[v>tr[p].val]=x;
	  		tr[x].init(p,v);
	  	}
	  	splay(x,0);
	  }
	  int getpre(int v){
	  	find(v);
	  	int x=root;
	  	if(tr[x].val<v) return x;
	  	x=ls(x);
	  	while(rs(x)) x=rs(x);
	  	splay(x,0);
	  	return x;
	  }
	  int getsuc(int v){
	  	find(v);
	  	int x=root;
	  	if(tr[x].val>v) return x;
	  	x=rs(x);
	  	while(ls(x)) x=ls(x);
	  	splay(x,0);
	  	return x;
	  }
	  void del(int v){
	  	int pre=getpre(v), suc=getsuc(v);
	  	splay(pre,0); splay(suc,pre);
	  	int del=ls(suc);
	  	if(tr[del].cnt>1) tr[del].cnt--,splay(del,0);
	  	else ls(suc)=0,splay(suc,0);//
	  }
	  int getrank(int v){ //排名
	  	insert(v);
	  	int res=tr[ls(root)].siz;
	  	del(v);
	  	return res;
	  }
	  int getval(int k){
	  	++k;
	  	int x=root;
	  	while(true){
	  		if(k<=tr[ls(x)].siz) x=ls(x);
	  		else if(k<=tr[ls(x)].siz+tr[x].cnt) break;
	  		else k-=tr[ls(x)].siz+tr[x].cnt, x=rs(x);
	  	}
	  	splay(x,0);
	  	return tr[x].val;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	insert(-INF);insert(INF);
	  	int n,op,x;cin>>n;
	  	while(n--){
	  		cin>>op>>x;
	  		if(op==1) insert(x);
	  		else if(op==2) del(x);
	  		else if(op==3) cout<<getrank(x)<<endl;
	  		else if(op==4) cout<<getval(x)<<endl;
	  		else if(op==5) cout<<tr[getpre(x)].val<<endl;
	  		else cout<<tr[getsuc(x)].val<<endl;
	  	}
	  	return 0;
	  }
	  ```
- 有注释模版:
	- ```C++
	  #include<bits/stdc++.h>
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  #define INF 0x3f3f3f3f3f3f3f3f
	  #define rep(i,j,k) for (int i=j;i<=k;++i)
	  #define per(i,j,k) for (int i=j;i>=k;--i)
	  const int mod=1e9+7;
	  const int N=2e5+5;
	  #define ls(x) tr[x].s[0]
	  #define rs(x) tr[x].s[1]
	  struct node{
	  	int s[2],fa,val,cnt,siz;
	  //左右儿,父,点权,个数,子树大小
	  	void init(int p,int v){
	  		fa=p, val=v;
	  		cnt=siz=1;
	  	}
	  }tr[N];
	  int root,tot;//根,节点数
	  void pushup(int x){tr[x].siz=tr[ls(x)].siz+tr[rs(x)].siz+tr[x].cnt;}//上传,更新siz信息
	  void rotate(int x){//旋转
	  	int y=tr[x].fa, z=tr[y].fa;
	  	int k=(tr[y].s[1]==x);
	  	tr[y].s[k]=tr[x].s[k^1], tr[tr[x].s[k^1]].fa=y;//z的儿是x,x的父是z
	  	tr[x].s[k^1]=y, tr[y].fa=x;//y的儿是x的异儿,x的异儿的父是y
	  	tr[z].s[tr[z].s[1]==y]=x, tr[x].fa=z;//x的异儿是y,y的父是x
	  	pushup(y),pushup(x);//维护信息
	  }
	  void splay(int x,int k){//伸展
	  	while(tr[x].fa!=k){//折线转xx,直线转yx
	  		int y=tr[x].fa, z=tr[y].fa;
	  		if(z!=k) (ls(y)==x)^(ls(z)==y)?rotate(x):rotate(y);
	  		rotate(x);
	  	}
	  	if(!k) root=x;//k=0时,x转到根
	  }
	  void find(int v){//找到v并转到根
	  	int x=root;
	  	while(tr[x].s[v>tr[x].val]&&v!=tr[x].val)
	  		x=tr[x].s[v>tr[x].val];
	  	splay(x,0);
	  }
	  void insert(int v){//插入
	  	int x=root, p=0;
	  	//x走到空节点或走到目标点结束
	  	while(x&&tr[x].val!=v) p=x,x=tr[x].s[v>tr[x].val];
	  	if(x) tr[x].cnt++;//目标点情况
	  	else{//空节点情况
	  		x=++tot;
	  		tr[p].s[v>tr[p].val]=x;
	  		tr[x].init(p,v);
	  	}
	  	splay(x,0);
	  }
	  int getpre(int v){//前驱
	  	find(v);
	  	int x=root;
	  	if(tr[x].val<v) return x;
	  	x=ls(x);
	  	while(rs(x)) x=rs(x);
	  	splay(x,0);
	  	return x;
	  }
	  int getsuc(int v){//后继
	  	find(v);
	  	int x=root;
	  	if(tr[x].val>v) return x;
	  	x=rs(x);
	  	while(ls(x)) x=ls(x);
	  	splay(x,0);
	  	return x;
	  }
	  void del(int v){//删除
	  	int pre=getpre(v), suc=getsuc(v);
	  	splay(pre,0); splay(suc,pre);
	  	int del=ls(suc);
	  	if(tr[del].cnt>1) tr[del].cnt--,splay(del,0);
	  	else ls(suc)=0,splay(suc,0);//
	  }
	  int getrank(int v){//排名
	  	insert(v);
	  	int res=tr[ls(root)].siz;
	  	del(v);
	  	return res;
	  }
	  int getval(int k){//数值
	  	++k;
	  	int x=root;
	  	while(true){
	  		if(k<=tr[ls(x)].siz) x=ls(x);
	  		else if(k<=tr[ls(x)].siz+tr[x].cnt) break;
	  		else k-=tr[ls(x)].siz+tr[x].cnt, x=rs(x);
	  	}
	  	splay(x,0);
	  	return tr[x].val;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	insert(-INF);insert(INF);//哨兵
	  	int n,op,x;cin>>n;
	  	while(n--){
	  		cin>>op>>x;
	  		if(op==1) insert(x);
	  		else if(op==2) del(x);
	  		else if(op==3) cout<<getrank(x)<<endl;
	  		else if(op==4) cout<<getval(x)<<endl;
	  		else if(op==5) cout<<tr[getpre(x)].val<<endl;
	  		else cout<<tr[getsuc(x)].val<<endl;
	  	}
	  	return 0;
	  }
	  ```
- 