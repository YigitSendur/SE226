#include <iostream>

using namespace std;

double pow(int n,int r) {
    if (r==0) return 1.0;
    return n * pow(n,r-1);
}
double calculateGn(int a,int b) {
    if (b==0) return 1.0;
    return pow(a,b)+calculateGn(a,b-1);
}

int main() {
    int n;
    int r;
    cout<<"Enter number (a): ";
    cin>>n;
    cout<<"Enter number (b): ";
    cin>>r;

    double sonuc = calculateGn(n,r);

    cout<<"Gn = "<<sonuc<<endl;
    return 0;
}