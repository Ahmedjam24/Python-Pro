#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
  int a1,*b;
  scanf("%d",&a1);
  b=malloc(a1*sizeof(int));
  for(int i=0;i<a1;i++)
  {
    scanf("%d",&b[i]);
  }
  int c[a1];
  for(int i=0;i<a1;i++)
  {
    int d=0,flag=0;
    for(int j=0;j<a1;j++)
    {
      if(j>i && flag==0)
      {
        if(b[j]>b[i])
        {
        d++;
        }
        else
        {
         flag=1; 
        }
      }      
    }
    c[i]=d+1;
  }
  int f=c[0];
  for(int i=0;i<a1;i++)
  {
    if(f<c[i])
    {
      f=c[i];
    }
  }
  printf("%d",f);
  return 0;
}
