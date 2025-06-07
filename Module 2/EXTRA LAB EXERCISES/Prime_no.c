/*3. Loops */
/*LAB EXERCISE 1: Prime Number Check 
 
• Write a C program that checks whether a given number is a prime number or not using a for 
loop. 
• Challenge: Modify the program to print all prime numbers between 1 and a given number. */
#include<stdio.h>
int main()
{
    int num,flag,sum=0,i,j;
    printf("\n Enter Number :");
    scanf("%d",&num);
    for ( i = 2; i <=num; i++)
    {
       flag = 1;
       for (j = 2; j <=i/2 ; j++)
       {
            if (i % j == 0)
            {
                flag = 0;
                break;
            }
        }
        if (flag == 1)
        {
            sum = sum + i;
            printf(" %d",i);
        }
     }
     printf("\n Sum of Prime Number : %d is %d",num,sum);
    
    return 0;
}