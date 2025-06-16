/*LAB EXERCISE 1: Fibonacci Sequence 
• Write a C program that generates the Fibonacci sequence up to N terms using a 
recursive 

function. 
• Challenge: Modify the program to calculate the N th Fibonacci number using both iterative 
and recursive methods. Compare their efficiency. */
#include<stdio.h>
int main()
{
    int term, first = 0, second = 1,i,next;
    printf("\n Enter Term:");
    scanf("%d",&term);
    for ( i = 1; i < term-2; i++)
    {
        next = first + second;
        second = first;
        first = next;
    }
    
    printf("\n Fibonacci Number :%d",next);
    
    
       return 0;
}