/*LAB EXERCISE 2: Check Number Properties 
 
• Write a C program that takes an integer from the user and checks the following using 
different operators: 
o Whether the number is even or odd. 
o Whether the number is positive, negative, or zero. 
o Whether the number is a multiple of both 3 and 5. */
#include<stdio.h>
int main()
{
    int num;
    printf("Enter a Number : ");
    scanf("%d",&num);

    printf("\n ---------EVEN OR ODD----------- ");

    if(num%2!=0)
    {
        printf("\n Number is Even : %d",num);
    }
    else
    {
         printf("\n Number is Odd : %d",num);
    }

    printf("\n ---------POSITIVE NEGATIVE OR ZERO----------- ");  

    if(num > 0)
    {
        printf("\n Number is Positive : %d",num);
    } 
    else if(num < 0)
    {
        printf("\n Number is Negative : %d",num);
    } 
    else{
        printf("\n Number is Zero : %d",num);
    }

    printf("\n ---------MULTIPLE 3 AND 5----------- ");

    if(num%3 == 0 && num%5 == 0)
    {
        printf("\n %d is a multiple of both 3 and 5", num);
    }
    else
    {
        printf("\n%d is not a multiple of both 3 and 5", num);
    }
    return 0;
}