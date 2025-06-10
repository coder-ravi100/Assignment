/*LAB EXERCISE 2: Multiplication Table 
 
• Write a C program that takes an integer input from the user and prints its multiplication 
table using a for loop. 
• Challenge: Allow the user to input the range of the multiplication table (e.g., from 1 to N). 
*/
#include<stdio.h>
int main()
{
    int num,i;
    printf("\n Enter the Number :");
    scanf("%d",&num);
    for(i=1;i<=10;i++)
    {
        printf("\n  %d X %d = %d",num,i,num*i);
        //10  X  1 = 10
    }
    return  0;
}