
#include<bits/stdc++.h>
using namespace std;

bool comparator(vector<float> a,vector<float> b)
{
    if(a[2]<=b[2])
       return 0;

    else return 1;

}


int main()
{
   vector<float> p(7);
   vector<float> w(7);
   vector<float> r(7);
   vector<vector<float> > vec;

   for(int i=0;i<7;i++)
   {
      cout<<"Enter profit:"<<endl;
      cin>>p[i];
      cout<<"Enter weight:"<<endl;
      cin>>w[i];
      r[i]=p[i]/w[i];

   }

   for(int i=0;i<7;i++)
   {
       vector<float> a;
       a.push_back(p[i]);
       a.push_back(w[i]);
       a.push_back(r[i]);

       vec.push_back(a);
  }
     sort(vec.begin(),vec.end(),comparator);

       for(int i=0;i<7;i++)
           cout<<vec[i][0]<<" "<<vec[i][1]<<" "<<vec[i][2]<<endl;

       int weight=15;
       float profit=0;

       for(int i=0;i<7;i++)
       {
          if(vec[i][1]<weight)
          {
             profit=profit+vec[i][0];
             weight=weight-vec[i][1];
          }

          else if(weight>0)
          {
            profit=profit+(weight/vec[i][1])*vec[i][0];
            weight=weight-vec[i][1];
          }

          else break;
       }

           cout<<profit;
     }
