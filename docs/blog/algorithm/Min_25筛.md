---
title: Min_25筛
date: 2025-07-31
category: 数论
tags:
  - 算法
outline: deep
---

## 详解:- ## ① Min_25筛概述
Min_25 用于求积性函数前级和 $\sum_{i=1}^n f(i)$，时间复杂度约为:$O\left(\frac{n^{\frac{3}{4} }}{\log n}\right) \quad (1e10\ 1s)$
要求:
* $f(p)$ 是一个关于素数 $p$ 的项数较小的多项式或能快速求值；
* $f(p^c)$ 可以快速求值。
  ---
## ② 推导(质数部分)
$h = \sum_{i=1}^{n} f(i)$
将 $h$ 分为合数和质数两个部分来清算：
先求质数:
在求质数时，我们需要一个完全积性函数 $F$，这与我们后面的推导有关，即
$F(p) = f(p)$ 在质数时。
然后有一个神仙 dp:
$$ g(n, j) = \sum_{i=1}^n F(i) \quad [i \text{是质数 或者最小因子大于第 } j \text{ 个素数}] $$
(注意在 $g(n, +\infty)$ 时，$\sum_{i=1}^n F(i) = \sum_{i=1}^n f(i)$)
我们最后要用到的就是 $g(n, +\infty)$。
这里不需要去真正的无穷，取尽就好
因为在 $\sqrt{n}$ 以内，没有合数的最小因子能 $> \sqrt{n}$ 了
  ---

$$
g(n, j) = \sum_{i=1}^n F(i) \quad \left[i \in \mathbb{P} \parallel \text{最小质因子大于第 } j \text{ 个素数}\right]
$$
考虑 $g(n, j)$ 的状态转移：
当 $p_j \leq \sqrt{n}$ 时（即 $p_j^2 \leq n$）
从 $g(n, j-1)$ 转移到 $g(n, j)$ 必然要减小，且减小的值就是最小质因子为 $p_j$ 的合数的值。
* $j-1$ 要求所有数的最小质因子 $\min_p > j-1$
* $j$ 要求所有数的最小质因子 $\min_p > j$
所以被减去的就是最小质因子为 $p_j$ 的合数。
注意：$p_j$ 是质数，一定要保留用于计算。
示例：以 $\text{id}(x)$ 为例：
g(25, 1) = 2\ 3\ 4\ 5\ 6\ 7\ 8\ ==9==\ 10\ 11\ 12\ 13\ 14\ ==15==\ 16\ 17\ 18\ 19\ 20\ ==21==\ 22\ 23\ 24\ ==25==
g(25, 2) = 2\ 3\ 4\ 5\ 6\ 7\ 8 \ 9 \ 10\ 11\ 12\ 13\ 14 \ 15 \ 16\ 17\ 18\ 19\ 20\ 21 \ 22\ 23\ 24\ ==25==
这些合数不妨设为 $x$，它们的值为 $F(x)$。
可以表示成 $F(x) = F(p_j) \cdot F\left(\frac{x}{p_j}\right) \quad \text{（完全积性函数）}$
$$
g(n,j) =
\begin{cases}
g(n,j-1) & p_j^2 > n \\
g(n,j-1) - F(p_j) \cdot \left(g\left(\left\lfloor \frac{n}{p_j} \right\rfloor,j-1\right) - \sum_{i=1}^{j-1} F(p_i)\right) & p_j^2 \leq n
\end{cases}
$$
这部分的时间复杂度被证明是:
$$
O\left(\frac{n^{\frac{3}{4} }}{\log n}\right)
$$
  ---
现在来加上合数部分统计答案：
我们引入一个新的综合:
$$ S(n, i) = \sum_{i=1}^{n} f(i) \quad [i\text{ 的最小因子大于第 } i \text{ 个质数}] $$
注意这里回到了 $f$ 的计算，只用到了积性函数的性质
我们最终要求的答案是:
$S(n, 0) + f(1)$
  ---
现在考虑怎么计算 $S$:
先列出定律，然后我们步步分析：
$$ S(n, i) = g(n, |P|) - \sum_{i=1}^{j-1} f(p_i) + \sum_{k=j+1}^{|P|} \sum_{e=1}^{\infty} f(p_k^e) \cdot \left(S\left(\left\lfloor \frac{n}{p_k^e} \right\rfloor, k\right) + [e > 1]\right) $$
$g(n, |P|)$ 只保留了 $\leq n$ 以内的质数和
$S(n, i)$ 要求的是最小因子大于第 $j$ 个素数
所以我们把第 $j$ 个质数的前级和减去，所以式子的前半部分就是质数对 $S$ 的贡献。
- ---
## ③推导(合数部分)
- 然后考虑合数,从 $(j+1)$ 个质数（记为 $(p_k)$）开始枚举一个合数的最小质因子。
一个数可能是同一个质数的多次幂，所以还要枚举幂。
并依次枚举 $(p_k^2, p_k^3, \dots, p_k^e)$ 直到 $(p_k^e \leq n)$。
有可能一个数只是这个质数的次方，它不会被 S 计算。而且 $e$ 应大于 1，否则它会算上这个质数。
这样的质数枚举到 $(p_k^2 \leq n)$ 就好。
这里的 f 和 S 可以直接相乘是利用了积性函数的性质，S 的设置保证了 f 和 S 是互质的。
  ---
## ④ 代码实现
这里用洛谷 P5325 作为模板实现代码：
计算积性函数 $f(x)$ 的前缀和与 $\sum_{i=1}^{n} f(i)$，其中对于质数 p 有：$f(p^k) = p^k (p^k - 1)$ 答案对 $(10^9 + 7)$ 取模。
$$
g(n, j) =
\begin{cases}
g(n, j-1) & p_j^2 > n \\
g(n, j-1) - F(p_j) \cdot \left(g\left(\left\lfloor \frac{n}{p_j} \right\rfloor, j-1\right) - \sum_{i=1}^{j-1} F(p_j)\right) & p_j^2 \leq n
\end{cases}
$$
$$
S(n, j) = g(n, |P|) - \sum_{i=1}^{j} f(p_i) + \sum_{k = j + 1}^{|P|} \sum_{\substack{e \geq 1 \\ p_k^e \leq n} } f(p_k^e) \left(S\left(\left\lfloor \frac{n}{p_k^e} \right\rfloor, k \right) + [e > 1]\right)
$$
根据这两个公式我们需要预处理：
- $\sum_{i=1}^{j-1} F(p_j)$ —— F 函数质数前缀和。注意 F 我们不用构造，用代替一下就好了。
- n 的整数分块的所有可能。
- $g(n, 0)$ 这样我们才能开始递推。
  ---
## ④ 代码实现（续）
- $\sum_{i=1}^{j-1} F(p_j)$：F 函数质数前缀和。注意 F 我们不用构造，用代替一下就好了。
注意到 $f(p^1) = p1(p1 - 1) = p^2 - p$。我们把 $(p^2)$ 和 $(p)$ 分别求前缀和放到 `sp1[]`, `sp2[]`。
另外，我们取 $+\infty$ 为 $\sqrt{n}$。在线性筛的时候顺便求出 `sp1[]`, `sp2[]`：
  ---
- n 的整数分块的所有可能。
使用整数分块优化时，对于 n，它整数分块的值约有 $\sqrt{n}$ 个。
我们用 w[] 保存这些值，tot 记为 $[1, \text{tot}]$。
同时，使用 id1[], d2[] 两个数组保存它们在 w 中的下标。
- id1[] 是 $\left\lfloor \frac{n}{x} \right\rfloor \leq \sqrt{n}$ 时的下标。
- id2[] 是 $\left\lfloor \frac{n}{x} \right\rfloor > \sqrt{n}$ 时的下标。
因为大于 $\sqrt{n}$ 的值可能会很大，所以反过来用 $(\frac{n}{l})$ 来保存 l 的下标。
这样将空间复杂度限制在 $(\sqrt{n})$ 以内。
  ---
- $g(n, 0)$：这样我们才能开始递推。
在预处理整数分块时，可以求出 $g_1(n, 0), g_2(n, 0)$，然后才能从 $(0)$递推到 $+\infty \ (sqrt{n})$。
在递推时，$g_1, g_2$ 都只需要一维，保存不同 n 的值即可，而且因为 n 是从大往小处理的，
所以前面的 n 的更改不会影响到后面的 $g_1, g_2$。
$g_1, g_2$ 用等差数列求和公式，注意 -1 因为 1 不符合 g 的条件。
## 板子1 (洛谷P5325):- # P5325 【模板】Min_25 筛
## 题目描述
定义积性函数 $f(x)$，且 $f(p ^ k) = p ^ k(p ^ k - 1)$（$p$ 是一个质数），求$$\sum_{i = 1} ^ n f(i)$$
对 $10 ^ 9 + 7$ 取模。
#### 输入格式
一行一个整数 $n$。
#### 输出格式
一个整数表示答案。
#### 输入1

```
10
```
#### 输出 2

```
263
```
#### 输入2
```
1000000000
```
#### 输出2

```
710164413
```
## 说明/提示
$f(1)=1$，$f(2)=2$，$f(3)=6$，$f(4)=12$，$f(5)=20$；  
$f(6)=12$，$f(7)=42$，$f(8)=56$，$f(9)=72$，$f(10)=40$。
对于 $30\%$ 的数据，保证 $1\le n\le 10^6$。
对于 $100\%$ 的数据，保证 $1\le n\le 10^{10}$。
## Code:

```C++
	  #include
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int mod=1e9+7;
	  const int N=2e5+5;
	  const int inv6=166666668;
	  bool prime[N];
	  int n;
	  int sq;//sq: √n,用于质数筛分界和整除分块
	  int cnt,p[N];//cnt: ≤sq的质数数量
	  int m,w[N];//m: 整除分块的块数, w[]:存储n/k（k整除分块时的值）
	  int id1[N],id2[N];//id1/id2: 对w中的数进行映射
	  int sum1[N],sum2[N];
	  int g1[N];//g1: w[i]内所有数的和（减1：去掉1）
	  int g2[N];//g2: w[i]内所有数的平方和（减1）
	  
	  /*需要知道f(p^k)=? (p是质数)*/
	  void EulerSieve(){
	  	for(int i=2;ix) return 0;
	  	int ans=((g2[getid(x)]+mod-g1[getid(x)])%mod+mod-(sum2[j]-sum1[j]+mod)%mod)%mod;
	  	//ans=(g[getid(x)] -sum[j] +mod)%mod;
	  	for(int i=j+1;i1))%mod)%mod;
	  			//ans=(ans + 新函数值f(sp) * (S(x/sp,i) + (e>1)) % mod) % mod;
	  	return ans;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	cin>>n;sq=sqrt(n);
	  	EulerSieve();
	  	for(int l=1,r;lw[m]}_f'(i) (将所有数视为质数)
	  		if(w[m] sq: 用id2[n/k]存下标
- **g1[]/g2[]**: 辅助数组，分别存储：
  - g1: w[i]内所有数的和（减1：去掉1）
  - g2: w[i]内所有数的平方和（减1）
- **mod**: 取模常数10^9+7
### 函数功能
	  1. **EulerSieve()**:
  - 线性筛出≤sq的所有质数存入p[]
  - 计算sum1和sum2数组（质数及平方前缀和）
		  
		  2. **f1(x)**:
  - 计算∑_{i=1}^{x} i = x(x+1)/2 mod mod
		  
		  3. **f2(x)**:
  - 计算∑_{i=1}^{x} i^2 = x(x+1)(2x+1)/6 mod mod
  - 166666668是6的模逆元（用于除法）
		  
		  4. **getid(x)**:
  - 根据x的大小，返回在id1或id2中的下标
  - 映射w[i]的索引
		  
		  5. **S(x, j)**:
  - 递归计算[1,x]内最小质因子>p[j]的函数值
  - **参数**：x为当前范围，j为质数索引
  - **返回**：∑_{i∈[1,x], i的最小质因子>p[j]} f(i)
  - 步骤：
  - 当p[j]>x时返回0
  - 质数部分：通过g2-g1计算大于p[j]的质数贡献
  - 合数部分：枚举最小质因子p[i]和指数e
    - sp = p[i]^e
    - 贡献 = sp(sp-1) * [S(x/sp, i) + (e>1)]
    - (e>1)确保当sp本身是合数时被计入
### 主流程
	  1. **预处理**:
  - 读入n，计算sq=√n
  - 筛质数并初始化sum1/sum2
		  
		  2. **整除分块**:
  - 计算所有n/k的值存入w[]，同时：
  - g1[i] = f1(w[i])-1 （去掉1）
  - g2[i] = f2(w[i])-1
  - 用id1/id2记录下标
			  
			  3. **DP更新g数组**:
  - 从小到大枚举质数p[i]
  - 用g[getid(w[j]/p[i])]更新g1[j]/g2[j]
  - 逐步筛去最小质因子≤p[i]的合数
		  
		  4. **递归计算答案**:
  - 调用S(n, 0)得到2~n的函数和
  - 结果+1（对应f(1) = 1）
### 算法特点
	  1. 时间：O(n^{3/4}/log n)，空间O(√n)
	  2. 优势：高效计算积性函数前缀和（特别适用于质数幂函数）
	  3. 实现技巧：
  - 整除分块压缩状态
  - id1/id2映射大数到连续数组
  - 积性拆分：f(n)=f1(n)+f2(n)
  - 递归处理质数贡献和合数贡献
## 板子2(小于等于n的素数个数):
- ```C++
	  #include
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=1e6+5;
	  bool prime[N];
	  int n;
	  int sq;//sq: √n,用于质数筛分界和整除分块
	  int cnt,p[N];//cnt: ≤sq的质数数量
	  int m,w[N];//m: 整除分块的块数, w[]:存储n/k（k整除分块时的值）
	  int id1[N],id2[N];//id1/id2: 对w中的数进行映射
	  int sum[N],g[N];
	  
	  /*需要知道f(p^k)=? (p是质数)*/
	  void EulerSieve(){
	  	for(int i=2;ix||j>cnt) return 0;
	  	int ans=(g[getid(x)]-sum[j]);
	  	return ans;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	cin>>n;
	  	sq=sqrt(n);
	  	EulerSieve();
	  	for(int l=1,r;lw[m]}_f'(i) (将所有数视为质数)
	  		if(w[m]<=sq) id1[w[m]]=m;
	  		else id2[n/w[m]]=m;
	  	}
	  	for(int i=1;i<=cnt;i++){
	  		for(int j=1;j<=m&&p[i]*p[i]<=w[j];j++){
	  			//g[j]=(g[j]+mod - f[p[i]]*(g[getid(w[j]/p[i])]-sum[i-1])%mod )%mod;
	  			g[j]=(g[j]-(g[getid(w[j]/p[i])]-sum[i-1]));
	  		}
	  	}
	  	cout<<S(n,0)<<endl;
	  	//(S(n,0)+f(1))%mod
	  	return 0;
	  }
```
```
```