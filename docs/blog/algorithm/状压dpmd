---
title: 状压DP
date: 2026-03-09
category: 动态规划
tags:
  - 算法
description: 状压DP相关的算法笔记和代码模板
---

### E25.小国王
	- ```C++
	  int n,k;
	  int cnt;
	  int s[1<<12];
	  int num[1<<12];
	  int f[12][144][1<<12];
	  //f[i][j][a]:前i行已经放了j个国王，第i行第a个状态时的方案数
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      cin>>n>>k;
	      for(int i=0;i<(1<<n);i++)
	          if(!(i&i>>1)){
	              s[cnt++]=i;
	              for(int j=0;j<n;j++)
	                  num[i]+=((i>>j)&1);
	          }
	      f[0][0][0]=1;
	      for(int i=1;i<=n;i++)//枚举行
	          for(int j=0;j<=k;j++)//枚举国王数
	              for(int a=0;a<cnt;a++)//枚举第i行的合法状态
	                  for(int b=0;b<cnt;b++){//枚举第i-1行的合法状态
	                      int c=num[s[a]];
	                      if((j>=c)&&!(s[a]&s[b])&&!(s[a]&(s[b]>>1))&&!(s[a]&(s[b]<<1)))
	                          f[i][j][a]+=f[i-1][j-c][b];
	                  }
	      int ans=0;
	      for(int i=0;i<cnt;i++) ans+=f[n][k][i];
	      cout<<ans<<endl;
	      return 0;
	  }
	  ```
-
- ### E26.玉米田
	- ```C++
	  const int mod=1e9+7;
	  int n,m;
	  int g[14];//地图限制
	  int cnt;//一行合法状态数量
	  int s[1<<14];//一行的合法状态
	  int f[14][1<<14];
	  //f[i][a]:已经种植前i行，第i行第a个状态时的方案数
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      cin>>n>>m;
	      for(int i=1;i<=n;i++){
	          for(int j=1;j<=m;j++){
	              int x;cin>>x;
	              g[i]=(g[i]<<1)+x;
	          }
	      }
	      for(int i=0;i<(1<<m);i++)//枚举一行中所有状态
	          if(!(i&i>>1)) s[cnt++]=i;
	      f[0][0]=1;
	      for(int i=1;i<=n+1;i++)
	          for(int a=0;a<cnt;a++)
	              for(int b=0;b<cnt;b++)
	                  if((s[a]&g[i])==s[a]&&!(s[a]&s[b])
	                  &&(s[b]&g[i-1])==s[b])
	                      f[i][a]=(f[i][a]+f[i-1][b])%mod;
	      cout<<f[n+1][0]<<endl;
	      return 0;
	  }
	  ```
- ### E27.炮兵部队
	- ```C++
	  const int N=110,M=1<<10;
	  int n,m,ans;
	  int g[N];
	  int cnt,s[M],num[M];
	  int f[2][M][M];
	  signed main(){
	      ios::sync_with_stdio(false);
	      cin.tie(nullptr);
	      cin>>n>>m;
	      for(int i=1;i<=n;i++)
	          for(int j=0;j<m;j++){
	              char c;cin>>c;
	              if(c=='P') g[i]+=1<<(m-j-1); 
	          }
	      for(int i=0;i<(1<<m);i++)
	          if(!(i&i>>1)&&!(i&i>>2)){
	              s[++cnt]=i;
	              for(int j=0;j<m;j++)
	                  num[i]+=(i>>j&1);
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