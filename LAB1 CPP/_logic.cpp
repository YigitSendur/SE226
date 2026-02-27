#include <iostream>
using namespace std;
int main() {
    int inp;
    cout<<"Enter your number: "<<endl;
    cin>>inp;
    int hours = inp/3600;
    int minutes = (inp-hours*3600)/60;
    int seconds = (inp-hours*3600-minutes*60);
    cout<<inp<<" Second is "<< hours <<" hours "<< minutes << " minutes "<< seconds <<" seconds "<<endl;
    return 0;


}