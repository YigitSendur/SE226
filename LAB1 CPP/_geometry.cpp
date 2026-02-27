#include <cmath>
#include <iostream>
#include <math.h>
using namespace std;
int main() {
    double x1,x2,y1,y2;
    cout<<"Enter the coordinates:"<<endl;
    cin>>x1>>y1>>x2>>y2;
    cout<<"x1: "<<x1<<endl;
    cout<<"y1: "<<y1<<endl;
    cout<<"x2: "<<x2<<endl;
    cout<<"y2: "<<y2<<endl;
    double distance=sqrt(pow(x2-x1,2)+pow(y2-y1,2));
    cout<<"distance: "<<distance<<endl;
    printf("*******\n"
           " *****\n "
           " ***\n "
           "  *");
    return 0;
}