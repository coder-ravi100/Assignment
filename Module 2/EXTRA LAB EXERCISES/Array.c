/*LAB EXERCISE 1: Maximum and Minimum in Array 
• Write a C program that accepts 10 integers from the user and stores them in an array. The 
program should then find and print the maximum and minimum values in the array. 
• Challenge: Extend the program to sort the array in ascending order.*/
#include<stdio.h>
int main(){
    
    int a[100],size,i,element,flag=1;
	printf("\nEnter the size of an array = ");
	scanf("%d",&size);
	for(i=0;i<size;i++)
	{
		printf("\nEnter the element in a[%d] = ",i);
		scanf("%d",&a[i]);
	}
	printf("\nEnter the element = ");
	scanf("%d",&element);//3
	for(i=0;i<size;i++)
	{
		if(element == a[i])
		{
			printf("\n%d is present on index %d",element,i);
           
			flag=0;
		}
	}
	if(flag==1)
	{
		printf("\nElement is not present in an array");
	}
    printf("\n Maximum Array = %d",a[size-1]);
    printf("\n Minimum Array = %d",a[0]);
    printf("\nSorted array in ascending order = ");
	for(i=0;i<size;i++)
	{
		printf("%d ",a[i]);
	}
    return 0;
}