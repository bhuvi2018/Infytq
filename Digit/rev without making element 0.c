#include <stdio.h>

int main() {
	int s,r=0,n=0,p=1;
	scanf("%d",&s);
	while(s>=p){
	    r=(s/p)%10;
	    n=n*10+r;
	    p=p*10;
	}
	printf("%d",n);
	return 0;
}
