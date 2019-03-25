#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
  int a2,*b2;
  scanf("%d",&a2);
  b2=malloc(a2*sizeof(int));
  for(int i=0;i<a2;i++)
  {
    scanf("%d",&b2[i]);
  }
  int c2[a2];
  for(int i=0;i<a2;i++)
  {
    int d2=0,flag2=0;
    for(int j=0;j<a2;j++)
    {
      if(j>i && flag2==0)
      {
        if(b2[j]>b2[i])
        {
        d2++;
        }
        else
        {
         flag2=1; 
        }
      }      
    }
    c2[i]=d2+1;
  }
  int f2=c2[0];
  for(int i=0;i<a2;i++)
  {
    if(f2<c2[i])
    {
      f2=c2[i];
    }
  }
  printf("%d",f2);
  return 0;
}
