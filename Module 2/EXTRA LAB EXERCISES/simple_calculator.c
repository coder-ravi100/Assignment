/*Write a C program that acts as a simple calculator. The program should take two numbers 
and an operator as input from the user and perform the respective operation (addition, 
subtraction, multiplication, division, or modulus) using operators. 
• Challenge: Extend the program to handle invalid operator inputs. 
*/

#include<stdio.h>
int main()
{
    int num1,num2,answer;
    printf("\n  Enter a number num1  :");
    scanf("%d",&num1);
    printf("\n  Enter a number num2  :");
    scanf("%d",&num2);

    int choice;
    char ch;
    printf("\n 1.Addision");
    printf("\n 2.Subtraction");
    printf("\n 3.Multiplication");
    printf("\n 4.Division");
    printf("\n 5.Remainder");  
    printf("\n Enter The Choice  :");
    scanf("%d",&choice);

    switch (choice)
    {
    case 1:
            printf("\n Addision is %d and %d is  : %d",num1,num2,num1+num2,answer);
    break;
    case 2:
            printf("\n Addision is %d and %d is  : %d",num1,num2,num1+num2,answer);
    break;
    }
    return 0;
}