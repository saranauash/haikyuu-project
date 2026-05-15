#include <iostream>
using namespace std;

bool f(int n){
    if(n==1) return 1;
    if(n<=0||n%2!=0) return 0;
    return f(n/2);
}

int main(){
    cout << (f(8)?"Yes":"No");
    return 0;
}