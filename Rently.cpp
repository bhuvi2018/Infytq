#include <iostream>
using namespace std;

int main() {
    int i=4;
    int j=--i;
    int k=i--;
	cout<<i<<" "<<j<<" "<<k;//output: 2 3 3 
	return 0;
}
