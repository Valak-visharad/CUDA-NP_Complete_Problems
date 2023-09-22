#include<stdio.h>
void Sum_Array()
{
    int ar[10000],n,sum=0;
    printf("Enter the limit \n");
    scanf("%d",&n);
    printf("Enter the array elements \n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    for(int i=0;i<n;i++)
    {
        sum=sum+ar[i];
    }
    printf("Sum of the array is %d",sum);
}
int main()
{
    Sum_Array();
    return 0;
}