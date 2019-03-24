#include <stdio.h>
int main()
{
    int n,k,ak[100],i,j,c=0;
    scanf("%d%d",&n,&k);
    for(i=0;i<n;i++)
    {
    	scanf("%d",&ak[i]);
    }
    for(i=0;i<n;i++)
    {  
    	for(j=i+1;j<n;j++)
    	{
    		if(ak[i]+ak[j]==k)
    		{
    			c++;
    		}
    	}
   	}
    if(c>=1)
    {
    	printf("yes");
    }
    else
    {
    	printf("no");
    }
	return 0; 
}
