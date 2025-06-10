/*Write a C program that acts as a simple calculator. The program should take two numbers 
and an operator as input from the user and perform the respective operation (addition, 
subtraction, multiplication, division, or modulus) using operators. 
• Challenge: Extend the program to handle invalid operator inputs. 
*/

#include<stdio.h>
int main()
{
    int num1,num2,answer;
    printf("\n  Enter a number 1  :");
    scanf("%d",&num1);
    printf("\n  Enter a number 2  :");
    scanf("%d",&num2);
    //char ch='%';
    char operators;
    printf("\n Enter the choice [+][-][*][/][%]");
    scanf(" %c",&operators);
    
    if(operators=='+')
    {
        printf("\n The Addition is :%d",answer=num1+num2);
    }
    else  if(operators == '-')
    {
        printf("\n The Minus is :%d",answer=num1-num2);
    }
    else if(operators == '*')
    {
        printf("\n The Multiplication is :%d",answer=num1*num2);
    }
    else if(operators == '/')
    {
        printf("\n The Division is :%d",answer=(float)num1/(float)num2);
    }
     if(operators == '%')
    {
        if(num1,num2%2!=0)
        {
                printf("\n The remainder is :%d",num1%num2);
        }
    }
   /* else
         {
                printf("\n Invalid Symbol Please try again....");
         } */
    
    return 0;
}