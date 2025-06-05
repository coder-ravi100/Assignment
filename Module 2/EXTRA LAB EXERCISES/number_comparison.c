 /*2.Number Comparison*/
/* Write a C program that takes three numbers from the user and determines: 
o The largest number. 
o The smallest number. 
• Challenge: Solve the problem using both if-else and switch-case statements.*/
#include<stdio.h>
int main()
{
    int num1,num2,num3;
    printf("\n Enter the Num 1 :");
    scanf("%d",&num1);
    printf("\n Enter the Num 2 :");
    scanf("%d",&num2);
    printf("\n Enter the Num 3 :");
    scanf("%d",&num3);

    
    if (num1 > num2)
        {
            printf("\n Largest Number is :%d",num1);
        }
        else if (num1 > num3)
        {
            printf("\n Largest Number is :%d",num3);
        } 
        if (num2 > num3)
        {

           printf("\n Largest Number is :%d",num2);
        }
        else
        {
          printf("\n Largest Number is :%d",num3);  
        }
               
    return 0;
}