/*LAB EXERCISE 3: Sum of Digits 
• Write a C program that takes an integer from the user and calculates the sum of its digits 
using a while loop. 
• Challenge: Extend the program to reverse the digits of the number.*/
#include<stdio.h>
int  main()
{
    int num,digit=0, rem,rev=0;
    printf("\n Enter The No:");
    scanf("%d",&num);
    while (num!=0)
    {
        rem = num % 10;
        rev = rev  * 10 + rem;
        num = num / 10;
        digit++;
    }
    printf("\n Sum Of Digits:%d",digit);
    //Challenge: Extend the program to reverse the digits of the number
    printf("\n Reverse No :%d",rev);
    
    return  0;
}