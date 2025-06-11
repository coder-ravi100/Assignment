/*LAB EXERCISE 2: Factorial Calculation 
• Write a C program that calculates the factorial of a given number using a function. 
• Challenge: Implement both an iterative and a recursive version of the factorial function and 
compare their performance for large numbers.*/
#include<stdio.h>
int fact()
{
    int num,fact=1,i;
    printf("\n Enter the Number :");
    scanf("%d",&num);
    for(i = 1; i <= num ;i++)
    {
        fact = fact * i;
    }
    return fact;
}
int main()
{
    int number;
    number = fact();
    printf("\n Factorial is :%d",number);
    return 0;
}