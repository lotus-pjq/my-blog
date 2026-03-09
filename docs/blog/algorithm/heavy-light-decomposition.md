---
title: 树链剖分完全指南：从理论到实战
date: 2026-03-09
category: 算法竞赛
tags:
  - 树链剖分
  - 图论
  - 线段树
  - 数据结构
  - 算法模板
description: 详解树链剖分的原理、实现和应用，包含完整的代码模板和复杂度证明。
---

# 树链剖分完全指南：从理论到实战

树链剖分（Heavy-Light Decomposition，简称 HLD）是处理树上路径问题的强大工具。

## 什么是树链剖分

树链剖分解决的是**在树上进行高效路径查询与修改**的问题，把**树结构转化为线性序列**，从而能够用线段树、树状数组等数据结构在 **O(log²n)** 的时间复杂度内完成：

- 路径查询/修改（如路径和、路径最大值）
- 子树查询/修改
- LCA（最近公共祖先）

---

## 核心思想

### 1. 重链剖分

将树的边分为**重边**和**轻边**：
- **重儿子**：子树节点数最多的儿子
- **轻儿子**：其他儿子
- **重边**：连接父节点和重儿子的边
- **轻边**：其他边

**重链**：由重边连接而成的极大路径。

### 2. DFS序

通过两次DFS，将树转化为线性序列：
- **第一次DFS**：处理 `fa`（父节点）、`dep`（深度）、`siz`（子树大小）、`son`（重儿子）
- **第二次DFS**：处理 `top`（所在重链的顶点）、`id`（DFS序编号）、`nw`（新编号对应的权值）

---

## 关键性质

### 性质1：重链数量

树上的一条路径一定被分割为**不超过 ⌊log₂ n⌋ + 1 条重链**。

**证明**：
- 每经过一条轻边，子树大小至少减半
- 最多经过 O(log n) 条轻边
- 每条轻边连接两条重链
- 因此重链数量为 O(log n)

### 性质2：DFS序的连续性

- 同一条重链上的节点在DFS序中是连续的
- 一个节点的子树在DFS序中是连续的

这两个性质使得我们可以用线段树高效维护。

---

## 代码实现

### 数据结构定义

```cpp
const int N = 2e5 + 5;

// 树的基本信息
int w[N];              // 原始权值
vector<int> e[N];      // 邻接表

// 第一次DFS处理的信息
int fa[N];             // 父节点
int dep[N];            // 深度
int siz[N];            // 子树大小
int son[N];            // 重儿子

// 第二次DFS处理的信息
int top[N];            // 所在重链的顶点
int id[N];             // DFS序编号
int nw[N];             // 新编号对应的权值
int cnt;               // DFS序计数器

// 线段树
struct tree {
    int l, r, add, sum;
} tr[N << 2];

int n, m, root, mod;
```

### 第一次DFS：处理基本信息

```cpp
void dfs1(int u, int fat) {
    fa[u] = fat;
    dep[u] = dep[fat] + 1;
    siz[u] = 1;
    
    for (int v : e[u]) {
        if (v == fat) continue;
        
        dfs1(v, u);
        siz[u] += siz[v];
        
        // 更新重儿子
        if (siz[son[u]] < siz[v])
            son[u] = v;
    }
}
```

### 第二次DFS：建立DFS序

```cpp
void dfs2(int u, int tp) {
    top[u] = tp;           // 记录重链顶点
    id[u] = ++cnt;         // 分配DFS序
    nw[cnt] = w[u];        // 记录新编号对应的权值
    
    // 优先处理重儿子（保证重链连续）
    if (son[u])
        dfs2(son[u], tp);
    
    // 处理轻儿子（每个轻儿子开启新的重链）
    for (int v : e[u]) {
        if (v == fa[u] || v == son[u]) continue;
        dfs2(v, v);  // 轻儿子作为新重链的顶点
    }
}
```

### 线段树基本操作

```cpp
#define ls (x << 1)
#define rs (x << 1 | 1)

void pushup(int x) {
    tr[x].sum = tr[ls].sum + tr[rs].sum;
}

void pushdown(int x) {
    if (tr[x].add) {
        tr[ls].sum += tr[x].add * (tr[ls].r - tr[ls].l + 1);
        tr[rs].sum += tr[x].add * (tr[rs].r - tr[rs].l + 1);
        tr[ls].add += tr[x].add;
        tr[rs].add += tr[x].add;
        tr[x].add = 0;
    }
}

void build(int x, int l, int r) {
    if (l == r) {
        tr[x] = {l, r, 0, nw[r]};
        return;
    }
    tr[x].l = l, tr[x].r = r;
    int mid = (l + r) >> 1;
    build(ls, l, mid);
    build(rs, mid + 1, r);
    pushup(x);
}

void update(int x, int l, int r, int k) {
    if (l > tr[x].r || r < tr[x].l) return;
    if (l <= tr[x].l && tr[x].r <= r) {
        tr[x].add += k;
        tr[x].sum += k * (tr[x].r - tr[x].l + 1);
        return;
    }
    pushdown(x);
    int mid = (tr[x].l + tr[x].r) >> 1;
    if (l <= mid) update(ls, l, r, k);
    if (r > mid) update(rs, l, r, k);
    pushup(x);
}

int query(int x, int l, int r) {
    if (l > tr[x].r || r < tr[x].l) return 0;
    if (l <= tr[x].l && tr[x].r <= r) return tr[x].sum;
    pushdown(x);
    return query(ls, l, r) + query(rs, l, r);
}
```

---

## 核心操作

### 1. 查询/修改子树

子树在DFS序中是连续的，直接操作区间 `[id[u], id[u] + siz[u] - 1]`。

```cpp
// 查询子树和
int query_tree(int u) {
    return query(1, id[u], id[u] + siz[u] - 1);
}

// 修改子树（所有节点权值加k）
void update_tree(int u, int k) {
    update(1, id[u], id[u] + siz[u] - 1, k);
}
```

**时间复杂度**：O(log n)

### 2. 查询/修改路径

路径可能跨越多条重链，需要跳链。

```cpp
// 查询路径和
int query_path(int u, int v) {
    int res = 0;
    
    // 当u和v不在同一条重链上
    while (top[u] != top[v]) {
        // 让深度较大的往上跳
        if (dep[top[u]] < dep[top[v]]) swap(u, v);
        
        // 查询u到其所在重链顶点的路径
        res += query(1, id[top[u]], id[u]);
        
        // 跳到重链顶点的父节点
        u = fa[top[u]];
    }
    
    // 此时u和v在同一条重链上
    if (dep[u] < dep[v]) swap(u, v);
    res += query(1, id[v], id[u]);
    
    return res;
}

// 修改路径（所有节点权值加k）
void update_path(int u, int v, int k) {
    while (top[u] != top[v]) {
        if (dep[top[u]] < dep[top[v]]) swap(u, v);
        update(1, id[top[u]], id[u], k);
        u = fa[top[u]];
    }
    if (dep[u] < dep[v]) swap(u, v);
    update(1, id[v], id[u], k);
}
```

**时间复杂度**：O(log²n)
- 跳链次数：O(log n)
- 每次线段树操作：O(log n)

---

## 完整模板

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl '\n'

const int N = 2e5 + 5;
#define ls (x << 1)
#define rs (x << 1 | 1)

int w[N];
vector<int> e[N];
int fa[N], dep[N], siz[N], son[N];
int top[N], id[N], nw[N], cnt;

struct tree {
    int l, r, add, sum;
} tr[N << 2];

int n, m, root, mod;

void pushup(int x) { tr[x].sum = tr[ls].sum + tr[rs].sum; }

void pushdown(int x) {
    if (tr[x].add) {
        tr[ls].sum += tr[x].add * (tr[ls].r - tr[ls].l + 1);
        tr[rs].sum += tr[x].add * (tr[rs].r - tr[rs].l + 1);
        tr[ls].add += tr[x].add;
        tr[rs].add += tr[x].add;
        tr[x].add = 0;
    }
}

void build(int x, int l, int r) {
    if (l == r) { tr[x] = {l, r, 0, nw[r]}; return; }
    tr[x].l = l, tr[x].r = r;
    int mid = (l + r) >> 1;
    build(ls, l, mid);
    build(rs, mid + 1, r);
    pushup(x);
}

void dfs1(int u, int fat) {
    fa[u] = fat, dep[u] = dep[fat] + 1, siz[u] = 1;
    for (int v : e[u]) {
        if (v == fat) continue;
        dfs1(v, u);
        siz[u] += siz[v];
        if (siz[son[u]] < siz[v]) son[u] = v;
    }
}

void dfs2(int u, int tp) {
    top[u] = tp, id[u] = ++cnt, nw[cnt] = w[u];
    if (son[u]) dfs2(son[u], tp);
    for (int v : e[u]) {
        if (v == fa[u] || v == son[u]) continue;
        dfs2(v, v);
    }
}

int query(int x, int l, int r) {
    if (l > tr[x].r || r < tr[x].l) return 0;
    if (l <= tr[x].l && tr[x].r <= r) return tr[x].sum;
    pushdown(x);
    return query(ls, l, r) + query(rs, l, r);
}

int query_tree(int u) {
    return query(1, id[u], id[u] + siz[u] - 1);
}

int query_path(int u, int v) {
    int res = 0;
    while (top[u] != top[v]) {
        if (dep[top[u]] < dep[top[v]]) swap(u, v);
        res += query(1, id[top[u]], id[u]);
        u = fa[top[u]];
    }
    if (dep[u] < dep[v]) swap(u, v);
    res += query(1, id[v], id[u]);
    return res;
}

void update(int x, int l, int r, int k) {
    if (l > tr[x].r || r < tr[x].l) return;
    if (l <= tr[x].l && tr[x].r <= r) {
        tr[x].add += k;
        tr[x].sum += k * (tr[x].r - tr[x].l + 1);
        return;
    }
    pushdown(x);
    int mid = (tr[x].l + tr[x].r) >> 1;
    if (l <= mid) update(ls, l, r, k);
    if (r > mid) update(rs, l, r, k);
    pushup(x);
}

void update_tree(int u, int k) {
    update(1, id[u], id[u] + siz[u] - 1, k);
}

void update_path(int u, int v, int k) {
    while (top[u] != top[v]) {
        if (dep[top[u]] < dep[top[v]]) swap(u, v);
        update(1, id[top[u]], id[u], k);
        u = fa[top[u]];
    }
    if (dep[u] < dep[v]) swap(u, v);
    update(1, id[v], id[u], k);
}

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m >> root >> mod;
    for (int i = 1; i <= n; i++) cin >> w[i];
    
    for (int i = 1, x, y; i < n; i++) {
        cin >> x >> y;
        e[x].push_back(y);
        e[y].push_back(x);
    }
    
    dfs1(root, 0);
    dfs2(root, root);
    build(1, 1, n);
    
    int op, x, y, z;
    while (m--) {
        cin >> op;
        if (op == 1) {
            cin >> x >> y >> z;
            update_path(x, y, z);
        } else if (op == 2) {
            cin >> x >> y;
            cout << query_path(x, y) % mod << endl;
        } else if (op == 3) {
            cin >> x >> y;
            update_tree(x, y);
        } else if (op == 4) {
            cin >> x;
            cout << query_tree(x) % mod << endl;
        }
    }
    
    return 0;
}
```

---

## 复杂度分析

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| 预处理（两次DFS） | O(n) | 建树 |
| 建线段树 | O(n) | |
| 子树查询/修改 | O(log n) | 单次线段树操作 |
| 路径查询/修改 | O(log²n) | 跳链O(log n) × 线段树O(log n) |
| 空间复杂度 | O(n) | |

---

## 应用场景

1. **路径查询/修改**：路径和、路径最大值、路径GCD等
2. **子树查询/修改**：子树和、子树最大值等
3. **LCA**：作为副产品，可以O(log n)求LCA
4. **树上差分**：结合差分思想处理树上区间问题
5. **树上DP优化**：某些树形DP可以用树链剖分优化

---

## 常见变种

### 1. 边权树链剖分

将边权转化为点权：
- 将边 (u, v) 的权值赋给深度较大的节点
- 查询路径时注意不要包含LCA

### 2. 树链剖分求LCA

```cpp
int LCA(int u, int v) {
    while (top[u] != top[v]) {
        if (dep[top[u]] < dep[top[v]]) swap(u, v);
        u = fa[top[u]];
    }
    return dep[u] < dep[v] ? u : v;
}
```

### 3. 树链剖分 + 其他数据结构

- 树链剖分 + 树状数组
- 树链剖分 + 平衡树
- 树链剖分 + 主席树

---

## 总结

树链剖分的核心思想：
1. **重链剖分**：将树分解为O(log n)条重链
2. **DFS序**：将树转化为线性序列
3. **数据结构维护**：用线段树等维护序列

掌握树链剖分后，大部分树上路径问题都能高效解决。

---

## 模板题

- P3384 【模板】树链剖分
- P2590 [ZJOI2008] 树的统计
- P3178 [HAOI2015] 树上操作

