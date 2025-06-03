/*Write a C program that acts as a simple calculator. The program should take two numbers 
and an operator as input from the user and perform the respective operation (addition, 
subtraction, multiplication, division, or modulus) using operators. 
• Challenge: Extend the program to handle invalid operator inputs. 
*/

#include<stdio.h>
int main()
{

	int num1,num2;
	char operators;
	printf("\n Enter the Number [1] :");
	scanf("%d",&num1);
	printf("\n Enter the Number [2] :");
	scanf("%d",&num2);
	printf("\n Enter The Operators [+][-][*][/] :");
	scanf(" %c",&operators);
	
	if(operators == '+')
	{
		printf("\n Addition  %d",num1+num2);
	}
	else if(operators == '-')
	{
		printf("\n Subtraction %d",num1-num2);
	}
	else if(operators == '*')
	{
		printf("\n Multiplication %d",num1*num2);
	}
	else if(operators == '/')
	{
		printf("\n Division %.2f",(float)num1/(float)num2);
	}
	else
	{
		printf("\n Invalid operator inputs");
	}
    return 0;
}