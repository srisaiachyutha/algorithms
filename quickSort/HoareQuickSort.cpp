#include<iostream>
using namespace std;

int partitionByHoare(int arr[],int left ,int right){
    int x=arr[left];
    int i=left-1;
    int j=right+1;

    while(1){
        do{
            j--;

        }while(arr[j]>x);
        do{
            i++;
        }while(arr[i]<x);
        if(i>=j){return j;
            
        }else
        {
            swap(arr[i],arr[j]);
        }
        
    }
    

}
void quickSortHoare(int arr[],int left,int right){
    if(left<right){
        int mid=partitionByHoare(arr,left,right);
        quickSortHoare(arr,left,mid-1);
        quickSortHoare(arr,mid+1,right);
    }
}

void printArray(int arr[],int n){
    for(int i=0;i<n;i++)
    cout<<arr[i]<<" ";
}


int main(){
    int arr[]={2,8,7,2,1,3,3,5,0,6,4};
    int n=sizeof(arr)/sizeof(int);
    cout<<"the assendign order is ";
    quickSortHoare(arr,0,n-1);
    printArray(arr,n);cout<<endl;
    

}