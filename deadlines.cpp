#include<bits/stdc++.h>
using namespace std;

bool compare(vector<int> a,vector<int> b)
{
    if(a[0]>=b[0])
      return 1;

      else return 0;
}

int main()
{
      vector<int> profits(5);
      vector<int> d(5);

      int ans=INT_MIN;

      for(int i=0;i<5;i++)
      {
          cout<<"Enter profit:"<<endl;
          cin>>profits[i];
          cout<<"Enter deadlines:"<<endl;
          cin>>d[i];
      }

      for(int i=0;i<5;i++)
           ans=max(ans,d[i]);

      vector<int> deadlines(ans+1,-1);

      vector<vector<int>> vec;

      for(int i=0;i<5;i++)
      {
          vector<int> r;
          r.push_back(profits[i]);
          r.push_back(d[i]);
          vec.push_back(r);
      }

      sort(vec.begin(),vec.end(),compare);
      for(int i=0;i<5;i++)

        cout<<vec[i][0]<<" "<<vec[i][1]<<endl;

      int profit=0;

      for(int i=0;i<5;i++)
      {
          int deadl=vec[i][1];

          if(deadlines[deadl]==-1)
          {
             profit=profit+vec[i][0];
             deadlines[deadl]=1;
             }

          else
          {
              for(int j=deadl-1;j>=1;j--)
              {
                  if(deadlines[j]==-1)
                  {
                      profit=profit+vec[i][0];
                      deadlines[deadl]=1;
                  }

              }

          }
      }
          for(int i=0;i<deadlines.size();i++)
             cout<<deadlines[i]<<" ";
             cout<<endl;
          cout<<profit;
}
