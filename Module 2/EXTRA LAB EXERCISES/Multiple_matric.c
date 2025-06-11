/*LAB EXERCISE 2: Matrix Addition 
• Write a C program that accepts two 2x2 matrices from the user and adds them. Display the 
resultant matrix. 
• Challenge: Extend the program to work with 3x3 matrices and matrix multiplication. */
#include<stdio.h>

int main()
{
    int a[10][10], b[10][10], ans[10][10];
    int size, i, j, k;

    printf("\n Enter the Row And Col Number = ");
    scanf("%d", &size);

    // Input for Matrix A
    printf("\nElement In Array A:\n");
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            printf("Enter the Element in a[%d][%d]: ", i, j);
            scanf("%d", &a[i][j]);
        }
    }

    // Input for Matrix B
    printf("\nElement In Array B:\n");
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            printf("Enter the Element in b[%d][%d]: ", i, j);  
            scanf("%d", &b[i][j]);
        }
    }

    // Multiplication logic
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            ans[i][j] = 0; // Initialize with 0
            for (k = 0; k < size; k++)
            {
                ans[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    // Display Matrix A
    printf("\nArray A := \n");
    for(i = 0; i < size; i++)
    {
        for(j = 0; j < size; j++)
        {
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }

    // Display Matrix B
    printf("\nArray B := \n");
    for(i = 0; i < size; i++)
    {
        for(j = 0; j < size; j++)
        {
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }

    // Display Result (Multiplication)
    printf("\nMultiplication of A and B := \n");  
    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }

    return 0;
}

