#include <stdio.h>
#include <stdlib.h>

void main()
{
    int m,n,i,j,l;
    printf("how many");
    scanf("%d",&m);
    int a[m];
    for (i=0;i<m;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("how many");
    scanf("%d",&n);
    int b[n];
    for(j=0;j<n;j++)
    {
        scanf("%d",&b[j]);
    }
    int c[m+n];
    i=0;
    j=0;
    l=0;
    for(l=0;l<m+n;l++)
    {
        if(i<m && j<n)
        {
            if(a[i]<b[j])
            {
                c[l]=a[i];
                i++;
            }
            else
            {
                c[l]=b[j];
                j++;
            }
        }
        else if(i<n)
        {
            c[l]=a[i];
            i++;
        }
        else
        {
            c[l]=b[j];
            j++;
        }
    }
    for (l=0;l<m+n;l++)
    {
        printf("%d\t",c[l]);
    }
}