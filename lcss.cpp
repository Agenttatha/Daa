#include<bits/stdc++.h>
using namespace std;


string lcs(string str1,string str2)
{
   int m=str1.length();
   int n=str2.length();

   int dp[m+1][n+1];

   for(int i=0;i<n+1;i++)
      for(int j=0;j<m+1;j++)
         dp[i][j]=0;


   for(int i=1;i<m+1;i++)
      for(int j=1;j<n+1;j++)
      {
          if(str1[i-1]==str2[j-1])
               dp[i][j]=dp[i-1][j-1]+1;

          else
             dp[i][j]=max(dp[i-1][j],dp[i][j-1]);

     }

     string res="";

     int i=m;int j=n;

     while(i>0 and j>0)
     {
        if(str1[i-1]==str2[j-1])
        {
           res+=str1[i-1];
           i=i-1;
           j=j-1;
        }

        else if(dp[i-1][j]>dp[i][j-1])
           i=i-1;

        else j=j-1;
     }
       return res;
}

int main()
{
   string str1="kalyan";
   string str2="ayn";

   string res=lcs(str1,str2);
   cout<<res;
}


