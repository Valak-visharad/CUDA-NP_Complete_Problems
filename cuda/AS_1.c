#include<stdio.h>
void prefixSum_CPU()
{
    int n;
    int ar[1000],pre_sum[1000];
    printf("Enter the array limits\n");
    scanf("%d",&n);
    printf("Enter the array elements\n");
    for(int i=0;i<n;i++)
    {
        scanf("%d",&ar[i]);
    }
    pre_sum[0]=ar[0];
    for(int i=1;i<n;i++)
    {
        pre_sum[i]=pre_sum[i-1] + ar[i];
    }
    for(int i=0;i<n;i++)
    {
        printf("%d ",pre_sum[i]);
    }
}
int main()
{
    prefixSum_CPU();
    return 0;
}