#include<stdio.h>
void reversal()
{
    int ar[5][5];
    printf("Enter the array elements \n");
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            scanf("%d",&ar[i][j]);
        }
    }
    printf("Array is - \n");
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<5;j++)
        {
            printf("%d\t",ar[i][j]);
        }
        printf("\n");
    }
    printf("Reversed Array is - \n");
    for(int i=0;i<5;i++)
    {
        for(int j=4;j>=0;j--)
        {
            printf("%d\t",ar[i][j]);
        }
        printf("\n");
    }
}
int main()
{
    reversal();
    return 0;
}
