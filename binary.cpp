# include<iostream>
using namespace std;
int main(){


    int arr[5]={1,2,3,4,5};
    int key=5;
    int mid;
    int i=0;
    int j=sizeof(arr)/sizeof(arr[0])-1;



    while(i<=j){
        mid=i+(j-1)/2;

        if (arr[mid]==key){


            cout<<"element persent at "<<mid;
            return 0;
        }

        else if(arr[mid]>key){

            j=mid-1;
        }

        else{

            i=mid+1;
        }



    }
    cout<<"element not found";



}