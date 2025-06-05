 /*2.Number Comparison*/
/* Write a C program that takes three numbers from the user and determines: 
o The largest number. 
o The smallest number. 
• Challenge: Solve the problem using both if-else and switch-case statements.*/
#include<stdio.h>
int main()
{
    int num1,num2,num3;
    int ch;
    printf("\n Enter the Num 1 :");
    scanf("%d",&num1);
    printf("\n Enter the Num 2 :");
    scanf("%d",&num2);
    printf("\n Enter the Num 3 :");
    scanf("%d",&num3);
    printf("\n 1. Press For Largest Number... ");
    printf("\n 2. Press For Smallest Number... ");
    printf("\n Enter The Choice");
    scanf("%d",&ch);
    switch (ch)
    {
    case 1:
    if (num1 > num2 && num1 > num3)
    {
        printf("\n Largest Number :%d",num1);
    }
    else if (num2 >= num1 && num2 >= num3)
    {
       printf("\n Largest Number :%d",num2);
    }
    else
    {
         printf("\n Largest Number :%d",num3);
    }
    break;
    case 2:
    if (num1 < num3  && num1 < num3)
    {
         printf("\n Smallest Number :%d",num1);
    }
    else if (num2 <= num1  && num2 <= num3)
    {
        printf("\n Smallest Number :%d",num2);
    }
    else
    {
        printf("\n Smallest Number :%d",num3); 
    }
    break;
    }
    return 0;
}