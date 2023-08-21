#include<bits/stdc++.h>
using namespace std;


void print_optimal_p(vector<vector<int>> par,int i,int j)
{

     if(i==j)
        cout<<"A"+i;
    else
    {
        cout<<"(";
        print_optimal_p(par, i, par[i][j]);
        print_optimal_p(par, par[i][j] + 1, j);
        cout<<")";

   }


}

int main()
{
   int n=4;
   vector<int> d(5);



   for(int i=0;i<5;i++)
      {
         cout<<"Enter dimensions:"<<endl;
         cin>>d[i];
      }

  vector<vector<int>>  cost(n+1,vector<int>(n+1));
  vector<vector<int>>  par(n+1,vector<int>(n+1));

  for(int i=1;i<n+1;i++)
  {
      for(int j=1;j<n+1;j++)

        if(i==j)
            cost[i][j]=0;;

  }

   int s=1;


   while(s<n+1)
   {

   for(int i=1;i<n+1;i++)
     {
        for(int j=1;j<n+1;j++)
        {
           if(j-i==s)
           {
              int ans=INT_MAX;
              for(int k=i;k<j;k++)
              {
                  ans=min(ans,cost[i][k]+cost[k+1][j]+d[i-1]*d[j]*d[k]);
                  cost[i][j]=ans;
               }
        }
     }
    }
       s++;
 }



   for(int i=1;i<n+1;i++)
   {
     for(int j=1;j<n+1;j++)
          cout<<cost[i][j]<<" ";

       cout<<endl;
    }


     cout<<endl;

}
