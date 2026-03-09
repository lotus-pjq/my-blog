---
title: Educational Codeforces Round 155 (Rated for Div. 2)
date: 2025-10-02
category: 数学
tags:
  - 算法
outline: deep
---

## C #组合数- 题目- 
- 思路- 
- 代码

```C++
#include
using namespace std;
#define rep(i,j,k) for (int i=j;i>s;
  int n=s.size();s=' '+s;
  int cnt=0;
  int ans=1,cur=0;
  rep(i,1,n-1){
    if(s[i]==s[i+1]) cnt++;
  }
  rep(i,1,n-1){
    if(s[i]!=s[i+1]){
      if(cur) ans=ans*(cur+1)%mod;
      cur=0;
    }else cur++;
  }
  if(cur) ans=ans*(cur+1)%mod;;
  cout>t;
  while(t--) solve();
  return 0;
}
```
## D #按位 #前缀- 题目
- 思路
- 代码
```C++
#include
using namespace std;
#define int long long
#define endl '\n'
#define rep(i,j,k) for (int i=j;i>n;
rep(i,1,n){
cin>>a[i];
a[i]^=a[i-1];
}
int ans=0,cur,sum0,sum1,cnt0,cnt1;
rep(i,0,32){
cur=sum0=sum1=cnt1=0,cnt0=1;
for(int j=1;j>i)&1){
cnt1++;
sum1=(sum1+j)%mod;
cur=(cur+(cnt0*j-sum0)%mod)%mod;
}else{
cnt0++;
sum0=(sum0+j)%mod;
cur=(cur+(cnt1*j-sum1)%mod)%mod;
}
}
//cout<<"TEST::"<<cur<<endl;
ans=(ans+(1<<i)*cur%mod)%mod;
}
cout<<ans<<endl;
return 0;
}

```
-