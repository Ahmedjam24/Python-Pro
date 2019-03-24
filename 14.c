#include <stdio.h>
int main()
{
	int n1,q,p[10],r[10],a[10],i1,j,k;
	scanf("%d %d",&n1,&q);
	for(i1=1;i1<=n1;i1++)
	{
	    scanf("%d",&a[i1]);
	}
	for(k=1;k<=q;k++)
	{
	    scanf("%d %d",&p[k],&r[k]);
	}
		for(k=1;k<=q;k++)
	{
	     int x=0;
	    for(i1=p[k];i1<=r[k];i1++)
	    {
	      x=x^a[i1];
	      
	    }
	   printf("%d\n",x);
	}

	    return 0;
}
