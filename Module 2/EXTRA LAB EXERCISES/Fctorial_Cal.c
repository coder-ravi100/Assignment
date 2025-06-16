/*LAB EXERCISE 2: Factorial Calculation 
• Write a C program that calculates the factorial of a given number using a function. 
• Challenge: Implement both an iterative and a recursive version of the factorial function and 
compare their performance for large numbers.*/
#include<stdio.h>
int fact(int num)
{

    int fact=1,i;
    for ( i = 1; i <= num; i++)
    {
        fact = fact * i;
    }
    return fact;
}
int main()
{
    int number,result;
    printf("\n Enter Value :");
    scanf("%d",&number);
    result = fact(number);
    printf("\n Factorial:%d",result);
    return 0;
}