#include<iostream>
#include<vector>
using namespace std;
void print(vector<int>& arr){
	for(int i=0;i<arr.size();i++)
		std::cout<<arr[i]<<" ";
}

void complete_remaining_comparisons(vector<int>& v,int index_starting, int& min, int& max){
	int n = v.size();
	for(int i = index_starting; i<n; i+=2){
			if(v[i]<=v[i+1]){
				if(v[i]<min)min = v[i];

				if(v[i+1]>max)max = v[i+1];
			}else{
				if(v[i+1]<min)min = v[i+1];

				if(v[i]>max)max = v[i];
			}

		}
}


int main(){

	int min,n=0,max,temp;
	std::vector<int> v;
	std::cout<<"enter the number of elements you want to enter [n>0]:";
	std::cin>>n;
	for(int i=0;i<n;i++){cin>>temp;v.push_back(temp);}
		print(v);
	if(n%2==1){
		min = v[0];
		max = v[0];
		complete_remaining_comparisons(v,1,min,max);
		
	}else{
		if(v[0]<=v[1]){
			min = v[0];
			max = v[1];
		}else{
			min = v[1];
			max = v[0];
		}
		complete_remaining_comparisons(v,2,min,max);
	}
	//print(v);
	cout<<min<<"\t"<<max;
}