#include <stdio.h>

int main() {
	int s,r=0,n=0,p=1,nn=0;
	int h,k;
	scanf("%d",&s);
	scanf("%d %d",&h,&k);
	while(s>=p){
	    r=(s/p)%10;
	    if(r==h)
	    r=k;
	    n=r*p+n;
	    p=p*10;
	}
	printf("%d",n);
	return 0;
}
//i/p:15093
//5
//8
//o/p:18093
