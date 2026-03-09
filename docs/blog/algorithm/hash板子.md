---
title: hash板子
date: 2025-10-27
category: 字符串
tags:
  - 算法
outline: deep
---

- Hash表
```C++
int T=0;
const int N=2e6+5;
const int M=262143;
struct E{int v;E*nxt;}*g[M+1],pool[N],*cur=pool,*p;int vis[M+1];
void ins(int v){
int u=v&M;
if(vis[u]nxt) if(p->v==v) return;
p=cur++;p->v=v;p->nxt=g[u];g[u]=p;
}
int ask(int v){
int u=v&M;
if(vis[u]nxt) if(p->v==v) return 1;
return 0;
}
void init(){T++,cur=pool;}
```
- 注释代码
```C++
const int N=2e6+5;//桶的大小，按需调整
const int M=262143;//M=0x3FFFF(18个1)
int T=0;//全局时间戳
struct E{
  int v;//存储的值
  E*nxt;//下一个节点指针
}*g[M+1],pool[N],*cur=pool,*p;
//g[M+1]: 哈希桶数组，每个桶是一个链表
//pool[N]: 预分配的内存池
//cur: 指向pool中下一个可用位置
//vis[M+1]: 标记桶是否在当前轮次被使用
//T: 时间戳，用于快速清空哈希表
int vis[M+1];
void ins(int v){
  int u=v&M;
  if(vis[u]nxt) if(p->v==v) return;//检查重复，保证元素唯一性
  p=cur++;p->v=v;p->nxt=g[u];g[u]=p;
}
bool ask(int v){
  int u=v&M;
  if(vis[u]nxt) if(p->v==v) return 1;
  return 0;
}
void init(){T++,cur=pool;}
```
-