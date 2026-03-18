#include <iostream>
using namespace std;

void swapValues(int* p1,int*p2) {
    int temp=*p1;
    *p1=*p2;
    *p2=temp;
}
void printArray(int* arr,int size) {
    for(int i=0;i<size;i++) {
        cout<<*(arr+i)<<" ";
    }
    cout<<endl;
}
int findMax(int* arr,int size) {
    int max = *arr;
    for (int i=1;i<size;i++) {
        if (*(arr+i)>max) {
            max = *(arr+i);
        }
    }
    return max;
}
void reverseArray(int* arr,int size) {
    int* start=arr;
    int* end=arr+size-1;
    while(start<end) {
        swapValues(start,end);
        start++;
        end--;
    }
}
int* createArray(int size) {
    return new int[size];
}
void deleteArray(int*arr) {
    delete[] arr;
    cout<<"memory was deleted"<<endl;
}
int main() {
    int size;
    cout << "Creating dynamic array..." << endl;
    cout << "Enter array size: ";
    cin >> size;

    int*myArray=createArray(size);
    cout<<"enter values"<<endl;
    for(int i=0;i<size;i++) {
        cin>>*(myArray+i);
    }
    cout<<"printing array"<<endl;
    printArray(myArray,size);

    cout<<"maximum element : "<<findMax(myArray,size)<<endl;
    cout<<"-----------------------"<<endl;
    cout<<"swapping two numbers : "<<endl;
    int a =5,b=8;
    cout << "Before swap" << endl << "a = " << a << endl << "b = " << b << endl;
    swapValues(&a, &b);
    cout << "After swap" << endl << "a = " << a << endl << "b = " << b << endl;

    cout << "----------------------------------" << endl;

    cout << "Reversing array..." << endl;
    reverseArray(myArray, size);
    cout << "Array after reverseArray:" << endl;
    printArray(myArray, size);

    cout << "----------------------------------" << endl;

    cout << "Deleting array..." << endl;
    deleteArray(myArray);

    return 0;

}