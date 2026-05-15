#include <iostream>
using namespace std;

void f(int n){
    if(n<=0) return;
    int v; cin>>v;
    f(n-1);
    cout<<v<<" ";}

int main(){
    f(3); 
    return 0;}