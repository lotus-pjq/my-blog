---
title: 状压DP
date: 2025-08-04
category: 动态规划
tags:
  - 算法
outline: deep
---

### E25.小国王
- ```C++
	  int n,k;
	  int cnt;
	  int s[1>n>>k;
	      for(int i=0;i>1)){
	              s[cnt++]=i;
	              for(int j=0;j>j)&1);
	          }
	      f[0][0][0]=1;
	      for(int i=1;i=c)&&!(s[a]&s[b])&&!(s[a]&(s[b]>>1))&&!(s[a]&(s[b]>n>>m;
	      for(int i=1;i>x;
	              g[i]=(g[i]>1)) s[cnt++]=i;
	      f[0][0]=1;
	      for(int i=1;i>n>>m;
	      for(int i=1;i>c;
	              if(c=='P') g[i]+=1>1)&&!(i&i>>2)){
	              s[++cnt]=i;
	              for(int j=0;j>j&1);
	          }
	      for(int i=1;i<=n;i++)
	          for(int a=1;a<=cnt;a++)
	              for(int b=1;b<=cnt;b++)
	                  for(int c=1;c<=cnt;c++)
	                      if(!(s[a]&s[b])&&!(s[a]&s[c])&&!(s[b]&s[c])
	                      &&(g[i]&s[a])==s[a]&&(g[i-1]&s[b])==s[b])
	                          f[i&1][a][b]=max(f[i&1][a][b],f[(i-1)&1][b][c]+num[s[a]]);
	      for(int a=1;a<=cnt;a++)
	          for(int b=1;b<=cnt;b++)
	              ans=max(ans,f[n&1][a][b]);
	      cout<<ans<<endl;
	      return 0;
	  }
	  ```