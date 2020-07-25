#include<iostream>
#include<vector>
using namespace std;
void printGraph(vector<vector<int> >& g){
    for(int i=0;i<g.size();i++){
        for(int j=0;j<g.size();j++){
            cout<<g[i][j]<<"\t";
        }

        cout<<endl;
    }
}
int main(){
    int n,temp;
    cout<<"enter the number of vertices in the graph: ";
    cin>>n;
    vector<vector<int> > graph;
    cout<<"enter the adjacency matrix \n";
    for(int i=0;i<n;i++){
        cout<<"enter the data for the vertex "<<i<<endl;
        //graph.push_back(new vector<int>);
        for(int j=0;j<n;j++){
            cin>>temp;
            graph[i].push_back(temp);
        }
    }
    printGraph(graph);


    return 0;
}