/*2. Control Statements*/

/*Write a C program that takes the marks of a student as input and displays the corresponding 
grade based on the following conditions: 
o Marks > 90: Grade A 
o Marks > 75 and <= 90: Grade B 
o Marks > 50 and <= 75: Grade C 
o Marks <= 50: Grade D 
• Use if-else or switch statements for the decision-making process. */
#include<stdio.h>
int main()
{
    int marks;
    printf("Enter the Marks :");
    scanf("%d",&marks);
    if (marks > 90)
    {
        printf("\n  Grade A ");
    }
    else if (marks > 75 && marks <= 90)
    {
       printf("\n  Grade B ");
    }
    else if (marks > 50 && marks <= 75)
    {
        printf("\n  Grade C ");
    }
    else
    {
       printf("\n  Grade D ");
    }
    
   return 0;
}
