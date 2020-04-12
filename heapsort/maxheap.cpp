#include<iostream>
#include<vector>
using namespace std;
void Max_Heapify(std::vector<int> &arr , int i , int vector_size){
	int largest;
	int left = 2*i+1;
	int right = 2*i+2;
	if( left< vector_size && arr[left] > arr[i] ){
		largest = left;

	}else{
		largest = i;
	}
	if( right< vector_size && arr[right] > arr[largest]){
		largest = right;
	}
	if( largest != i){
		int temp = arr[i];
		arr[i] = arr[largest];
		arr[largest] = temp;
		Max_Heapify(arr ,largest ,vector_size); 
	}
}
int Parent(int index){
	if(index == 0){
		return index;
	}
	if(index&1 == 1){
		return index/2;
	}else{
		return index/2-1;
	}
}
void Heap_Increase_key(std::vector<int> &arr, int index , int key){
	if(index >= arr.size()){
		cout<<"your are entering the index greater than the size of std::vector<int> \n";
	}else{
		if(key < arr[index]){
			cout<<"new key is smaller than the present key\n";
		}else{
			arr[index] = key;
			while(index>0 && arr[Parent(index)] < arr[index]){
				int temp = arr[index];
				arr[index] = arr[Parent(index)];
				arr[Parent(index)] = temp;
				index = Parent(index);
			}
		}
	}


}

void Max_Heap_Insert(std::vector<int> &arr, int key){
	arr.push_back(-INF);
	Heap_Increase_key( arr, arr.size()-1, key );
}

void Build_Max_Heap(std::vector<int> &arr ){
	for( int i = arr.size()/2 ; i>=0;i--){
		Max_Heapify(arr , i, arr.size());
	}
}

void Heap_sort( std::vector<int> &arr){
	Build_Max_Heap(arr);
	int vector_size = arr.size() ;
	for(int i = arr.size()-1; i>0 ;i--){
		int temp = arr[0];
		arr[0] = arr[i];
		arr[i] = temp;
		vector_size--;
		Max_Heapify(arr,0,vector_size);
	}
}
void print_array(std::vector<int> &v){
	for(int i =0; i<v.size();i++){
		cout<<v[i]<<" ";
	}
	cout<<endl;
}
void options(){
	cout<<"1: print heap\t2: Heap_sort\t3: Build_Max_Heap\t4: Max_Heap_Insert\nchoose from options\n";
}
int main(){
	int next_time  = 1,option;
	std::vector<int> arr;
	cout<<"enter the size of  vector : ";
	int size_of_vector, temp;
	cin>>size_of_vector;
	cout<<"enter the data into the  vector \n";
	for(int i=0 ; i<size_of_vector;i++){
		cin>>temp;
		arr.push_back(temp);
	}
	do{
		options();
		cin>>option;
	switch(option){
		case 1:
				print_array(arr);break;
		case 2:
				Heap_sort(arr);break;
		case 3:
				Build_Max_Heap(arr);break;
		case 4:
				cout<<"enter the key value : ";
				int key;
				cin>> key;
				Max_Heap_Insert(arr,key);break;
	}
	cout<<"if you want to conitue type '1' else '0'\n";
	cin>>next_time;
	}while(next_time);

	return 0;
}