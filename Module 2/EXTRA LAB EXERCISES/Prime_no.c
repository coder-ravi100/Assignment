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
    for ( i = 2; i <=num; i++) //this line 1 se number tak sabh check karega
    {
       flag = 1; // this line Aisa mante hai ki har number prime hai
       for (j = 2; j <=i/2 ; j++) //  prime no check karne keliye
       {
            if (i % j == 0)
            {
                flag = 0;//number divide hogaya to prime nahi hai
                break;
            }
        }
        if (flag == 1) //Agar number prime hai
        {
            sum = sum + i;//prime number ko sum mein store karega
            printf(" %d",i);
        }
     }
     printf("\n Sum of Prime Number : %d",sum);
    
    return 0;
}