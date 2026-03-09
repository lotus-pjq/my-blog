---
title: 最长上升子序列(LIS)
date: 2025-08-30
category: 其他
tags:
  - 算法
outline: deep
---

## 分析：
- 
- ## Code：
- ```C++
	  #include
	  using namespace std;
	  #define int long long
	  #define endl '\n'
	  const int N=1e6+5;
	  int a[N],b[N],len,n;
	  int find(int x){
	  	int l=1,r=len,mid;
	  	while(l>1;
	  		if(b[mid]>=x) r=mid-1;
	  		else l=mid+1;
	  	}
	  	return l;
	  }
	  signed main(){
	  	ios::sync_with_stdio(false);
	  	cin.tie(nullptr);
	  	cin>>n;
	  	for(int i=1;i>a[i];
	  	for(int i=1;ib[len]) b[++len]=a[i];
	  		else b[find(a[i])]=a[i];
	  	}
	  	cout<<len;
	  	return 0;
	  }
	  ```
-