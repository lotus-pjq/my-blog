---
title: xde的双哈希模板
date: 2025-08-05
category: 字符串
tags:
  - 算法
outline: deep
---

```C++
typedef unsigned long long ul;
template
struct Htb{
    static constexpr int M=1e7+19;
    int hd[M+3],to[N],ct;
    tp1 ed[N];tp2 w[N];
    static int hc(ul v){
        v^=v>7;
        return (v^(vfind(tp1 x){
        for(int i=hd[hc(x)];i;i=to[i])
            if(ed[i]==x)return mkp(w[i],true);
        return mkp(tp2(),false);
    }
    int operator[](tp1 x){
        int &p=hd[hc(x)];
        for(int i=p;i;i=to[i])
            if(ed[i]==x)return i;
        ed[++ct]=x,to[ct]=p;
        return p=ct;
    }
    void clear(){while(ct)hd[hc(ed[ct--])]=0;}
};
```
```C++
using ll=long long;
using ull=unsigned long long;
using LL=__int128_t;
template
struct Htb{
    static constexpr int M=1e7+19;  // 哈希表模数
    int hd[M+3],to[N],ct;           // 链表头指针、下一节点指针、元素计数
    tp1 ed[N];                      // 键存储数组
    tp2 w[N];                       // 值存储数组
    // 哈希计算函数
    static int hc(ull v){
        v^=v>7;  
        return (v^(v find(tp1 x){
        for(int i=hd[hc(x)];i;i=to[i])
            if(ed[i]==x) return mkp(w[i],true); // 返回值和存在标志
        return mkp(tp2(),false);     // 返回空值和不存在的标志
    }
    //返回键对应的值的索引
    int operator[](tp1 x){
        int &p=hd[hc(x)];           // 计算哈希位置
        for(int i=p;i;i=to[i])       // 检查现有节点
            if(ed[i]==x) return i;   // 返回已有索引
        ed[++ct]=x;                 // 创建新键
        to[ct]=p;                   // 链式存储
        return p=ct;                // 更新头指针，返回新索引
    }
    void clear(){while(ct) hd[hc(ed[ct--])]=0;}
};
```
### 深度解析哈希表模板：设计逻辑与高级用法
#### 🧠 核心设计思路
  采用**开链法哈希表**架构，关键数据结构：
```cpp
static constexpr int M = 1e7 + 19; // 桶数(大质数)
int hd[M+3];          // 桶头指针数组
int to[N];            // 链式索引数组
tp1 ed[N];            // 键存储区
tp2 w[N];             // 值存储区
int ct = 0;           // 元素计数器
```
#### 🔑 关键方法精析
  1. **哈希函数 `hc()`**
```cpp
static int hc(unsigned long v) {
  v ^= v > 7;  // 位混淆
  return (v^(v find(string key) {
  int pos = hc(key);
  for(int i=hd[pos]; i; i=to[i])
      if(ed[i]==key) return {w[i], true};
  return {Value(), false}; // 未找到返回默认值
}
```
  
  3. **插入/更新操作**
```cpp
void ins(string key, Value val) {
  int pos = hc(key);
  int& head = hd[pos];  // 桶头引用

  // 头插法
  ed[++ct] = key;      // 存储键
  to[ct] = head;       // 新节点指向原头节点
  w[ct] = val;         // 存储值
  head = ct;           // 更新头指针
}
```
  > 🔥 注意：会重复插入相同键（不检查唯一性）
  
  4. **下标运算符（最强大功能）**
```cpp
int operator[](string key) {
  int pos = hc(key);
  int& head = hd[pos];

  // 尝试查找
  for(int i=head; i; i=to[i])
      if(ed[i]==key) return i; // 返回已存在索引

  // 不存在则创建新节点
  ed[++ct] = key;      // 插入键
  to[ct] = head;       // 链入头部
  w[ct] = Value();     // ✨改进：初始化值
  return head = ct;    // 返回新索引
}
```
  
  5. **高效清空**
```cpp
void clear() {
  while(ct>0) {           // 倒序处理元素
      int pos = hc(ed[ct]); // 根据键计算桶位置
      hd[pos] = 0;        // 仅重置当前桶头
      ct--;               // 回退计数器
  }
}
```
#### 🚀 高级使用场景
  1. **自定义类型键**
```cpp
struct Point { int x, y; };

// 特化哈希函数
template<> 
int Htb::hc(unsigned long v) {
  Point p = *((Point*)&v);
  return (p.x*131 + p.y) % M;
}

// 使用
Htb pointMap;
pointMap.ins({1,2}, "origin");
```
  
  2. **统计频次（下标操作符妙用）**
```cpp
Htb freq;
vector words = {"a","b","a","c"};

for(auto& w : words) {
  int idx = freq[w]; // 隐式插入
  freq.w[idx]++;     // 直接写值区
}

// 等效于:
// freq.w[freq["a"]] = 3;
```
  
  3. **键值批量处理**
```cpp
// 遍历所有元素
for(int i=1; i keysToRemove;
for(int i=1; i lookup;

while(query--) {
  lookup.clear();  // 高效清空
  // 重新使用同一个哈希表
  lookup.ins(newKey, newValue);
  ...
}
```
#### ⚠️ 关键注意事项
  1. **键类型约束**
- 需满足隐式转换到 `unsigned long`
- 对于复杂类型（如字符串），需特化哈希函数：
```cpp
// 字符串哈希特化
template<>
int Htb::hc(string s) {
unsigned long h = 0;
for(char c : s) h = h*131 + c;
return h % M;
}
```

2. **内存陷阱**
```cpp
Htb table; // 分配内存：
                           // 桶数组: (1e7+3)*4 ≈ 40MB
                           // 键值数组: 500 * (4+ ?) 
```
- 桶数组`hd`占用：`(1e7+3)*4字节 ≈ 40MB`
- N值需谨慎设置（避免栈溢出）

3. **并发安全**
- ❗ 非线程安全设计
- 写操作需加锁：
```cpp
mutex mtx;
mtx.lock();
int idx = table[key];
table.w[idx] = newValue;
mtx.unlock();
```

4. **删除操作限制**
- 原生不支持删除操作
- 替代方案：标记删除法
```cpp
// 删除标记值
constexpr Value DELETED = /*特殊值*/; 

void remove(Key key) {
  int pos = hc(key);
  for(int i=hd[pos]; i; i=to[i]){
      if(ed[i]==key) w[i] = DELETED;
  }
}
```
#### 💡 推荐改进方案
  1. **动态扩容版**
```cpp
template
class DynamicHtb {
  vector hd;
  vector keys;
  vector vals;
  vector next;
  int capacity;

  void resize(int new_size){
      // ...动态桶数组和存储数组扩展...
  }
  // 其他方法保持类似逻辑...
};
```
  
  2. **增强安全性版**（在`operator[]`中初始化值）
```diff
- w[p=ct]=y; // 原版
	  + w[ct] = tp2{}; p=ct; // 初始化为默认值
```
#### 🏆 应用场景分析
  1. **算法竞赛优势**
```cpp
// 典型题目：两数之和
Htb seen;
for(int i=0; i userCache;

 // 获取用户数据（带缓存）
 UserProfile getProfile(UserID id) {
 int idx = userCache[id];
 if(userCache.w[idx].isValid) 
    return userCache.w[idx];

 // 缓存未命中
 UserProfile fresh = DB.fetch(id);
 userCache.w[idx] = fresh;
 return fresh;
 }
```

3. **高效去重系统**
```cpp
Htb dedupSystem;

bool isUnique(BigDataType data) {
if(dedupSystem.count(data)) 
   return false;

dedupSystem.ins(data, true);
return true;
}
```

通过理解这些设计细节和使用模式，开发者可以更好地利用该模板处理高吞吐键值访问需求，同时在算法竞赛中实现高效解题。💪🏻