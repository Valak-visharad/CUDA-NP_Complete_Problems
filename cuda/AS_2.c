#include<stdio.h>
void min_max()
{
    int ar[10000],min,max,n;
    printf("Enter the array limits\n");
    scanf("%d",&n);
    printf("Enter the array elements\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    min=ar[0],max=ar[0];
    for(int i=0;i<n;i++)
    {
        if(min>ar[i])
            min=ar[i];
    }
    for(int i=0;i<n;i++)
    {
        if(max<ar[i])
            max=ar[i];
    }
    printf("Maximum = %d ",max);
    printf("Maximum = %d ",min);
}
int main()
{
    min_max();
    return 0;
}