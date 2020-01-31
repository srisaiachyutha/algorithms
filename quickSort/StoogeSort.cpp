#include<iostream>
using namespace std;
void stoogeSort(int arr[],int i,int j){
    if(arr[i]>arr[j])
        swap(arr[i],arr[j]);
    if(i+1>=j)return;
    int k=(j-i+1)/3;
    stoogeSort(arr,i,j-k);
    stoogeSort(arr,i+k,j);
    stoogeSort(arr,i,j-k);
}
void printArray(int arr[],int n){
    for(int i=0;i<n;i++)
        cout<<arr[i]<<" ";

}

int main(){
    int arr[]={2,8,7,1,3,5,6,4};
    int n=sizeof(arr)/sizeof(int);
    cout<<"before sorting::";
    printArray(arr,n);
    
    stoogeSort(arr,0,n-1);
    cout<<endl<<"after sorting::";
    printArray(arr,n);
}