/*LAB EXERCISE 3: Sum of Array Elements 
• Write a C program that takes N numbers from the user and stores them in an array. The 
program should then calculate and display the sum of all array elements. 
• Challenge: Modify the program to also find the average of the numbers*/
#include<stdio.h>
int main()
{
    int a[100],b[100],ans[200],i,size;
    printf("\n Enter the Size Of Array:");
    scanf("%d",&size);
     printf("\n Element of A=");
    for ( i = 0; i < size; i++)
    {
        printf("\n Enter  the Element of a [%d]=",i);
        scanf("%d",&a[i]);
    }
    
    printf("\n Element of B=");  
    for ( i = 0; i < size; i++)
    {
        printf("\n Enter  the Element of b [%d]=",i);
        scanf("%d",&b[i]);
    }
    for ( i = 0; i < size; i++)
    {
        ans[i] = a[i] + b[i];
    }
    printf("\nElement Of A=");
    for ( i = 0; i < size; i++)
    {
        printf(" %d",a[i]);
    }
    printf("\nElement Of B=");
    for ( i = 0; i < size; i++)
    {
        printf(" %d",b[i]);
    }
    printf("\nSum Of A and B :");
    for ( i = 0; i < size; i++)
    {
        printf(" %d",ans[i]);
    }
    int total = 0;
    for (i = 0; i < size; i++)
{
    total = total + ans[i];
}

    printf("\n average of the numbers is :%.2f",(float)total/size);
    
    return 0;
}
/*Problems:
ans[i] – loop ke baahar likha hai, i ki value loop ke baad size ho jaati hai. 
So ans[i] = ans[size] which is invalid index (garbage value).
mein size / ans[i] likh rahe ho — par average ka matlab hota hai:*/