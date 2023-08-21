#include<bits/stdc++.h>
using namespace std;

class node
{
   public:
   char data;
   int freq;
   node *left;
   node *right;
};

string decode="";

void print_tree(node *root,string t)
{
   if(root==NULL){
     return;
     }

    if(root->left==NULL and root->right==NULL and root->data!='0'){
       decode+=t;
       cout<<root->data<<" "<<t<<endl;
    }


   print_tree(root->left,t+"0");
   print_tree(root->right,t+"1");

}

node* create_tree(node *root,priority_queue< pair<int,node*>, vector<pair<int,node*>>, greater<pair<int,node*>> >pq)
{

       while(pq.size()>1)
       {
          pair<int,node*> a=pq.top();
          int f=a.first;
          pq.pop();
          pair<int,node*> b=pq.top();
          f+=b.first;
          pq.pop();

          node *p=new node();
          p->freq=f;
          p->left=a.second;
          p->right=b.second;
          p->data='0';
          pq.push(make_pair(f,p));
       }

       pair<int,node*> s=pq.top();
       pq.pop();
       return s.second;
}


int main()
{
    string t;
    cout<<"enter message:";
    cin>>t;

    priority_queue< pair<int,node*>, vector<pair<int,node*>>, greater<pair<int,node*>> >pq;

    map<char,int> mp;

    for(int i=0;i<t.length();i++)
          mp[t[i]]++;

    for(auto it=mp.begin();it!=mp.end();it++)
    {
        node *pointer=new node();
        pointer->data=it->first;
        pointer->freq=it->second;
        pointer->left=NULL;
        pointer->right=NULL;

        pq.push(make_pair(it->second,pointer));
    }

    node *root=NULL;
    root=create_tree(root,pq);

    print_tree(root,"");
    cout<<decode<<endl;
    cout<<decode.length();

}
