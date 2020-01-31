#include<iostream>
using namespace std;

int partitionAssending(int arr[],int left ,int right){
    int x=arr[right];
    int i=left-1;
    for(int j=left;j<=right-1;j++){
        if(arr[j]<=x){
            i++;
            int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
        }
    }
    swap(arr[i+1],arr[right]);
    return i+1;
}
int partitionDecending(int arr[],int left ,int right){
    int x=arr[right];
    int i=left-1;
    for(int j=left;j<=right-1;j++){
        if(arr[j]>=x){
            i++;
            int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
        }
    }
    swap(arr[i+1],arr[right]);
    return i+1;
}
void quickSortAssending(int arr[],int left,int right){
    if(left<right){
        int mid=partitionAssending(arr,left,right);
        quickSortAssending(arr,left,mid-1);
        quickSortAssending(arr,mid+1,right);
    }
}
void quickSortDesending(int arr[],int left,int right){
    if(left<right){
        int mid=partitionDecending(arr,left,right);
        quickSortDesending(arr,left,mid-1);
        quickSortDesending(arr,mid+1,right);
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
    quickSortAssending(arr,0,n-1);
    printArray(arr,n);cout<<endl;
    cout<<"the decending order is "; 
    quickSortDesending(arr,0,n-1);
    printArray(arr,n);

}