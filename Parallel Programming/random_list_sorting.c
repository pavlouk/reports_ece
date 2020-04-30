// University of Patras
// Department of Electrical Engineering & Computer Engineering
// Parallel Processing 2019-2020

// This program creates N nodes of a linked list
// each containing an array of N unsigned short integers.

// The random elements are not created with the built-in rand() 
// function as this would require a lot of time, but with a user-specified 
// seed value, passed in each parallel iteration and calculated as a product 
// of the previous iteration. 

// The program then sorts in each node in the encapsulated  array
// and can be used later on to short a bigger array, if the number of nodes 
// represent the leaves of a binary tree.

// Each sorting segment utilizes the built-in qsort function.

// vendor_id       : AuthenticAMD
// cpu family      : 23
// model           : 24
// model name      : AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx
// cpu MHz         : 2100.000
// cache size      : 512 KB
// siblings        : 8
// cpu cores       : 4

// Compilation: gcc random_list_sorting.c -03 -fopenmp

// Execution: time ./a.out
// real    0m3.961s
// user    0m28.203s
// sys     0m0.766s

//***************************************************************
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <omp.h>b
// **************************************************************
// Array Size
#define Nnodes 1000
#define N 100000
//***************************************************************
typedef struct node
{
    unsigned short int A[N];
    struct node *next;
} NODE;
// initialize starting node
NODE *Top;
// randomly selected seed value
unsigned int seed = 666999666;
// **************************************************************
unsigned int randUint(void)
{
    // makes the named file-scope, namespace-scope, 
    // or static block-scope variables private to a thread.
#pragma omp threadprivate(seed)
    seed = seed * 119945 + 12345;

    return seed;
}
//***************************************************************
// This function is utilized by the qsort function 
int compar(const void *a, const void *b)
{
    if (*(unsigned short *)a > *(unsigned short *)b)
        return 1;
    if (*(unsigned short *)a < *(unsigned short *)b)
        return -1;
    else
        return 0;
}
//***************************************************************
NODE *createLinkList(void)
{
    NODE *ptop, *pcur;
    // first list element memory allocation 
    ptop = malloc(sizeof(NODE));
    // case it won't work
    if (ptop == NULL)
        return NULL;
    // proceed to the next one
    pcur = ptop;
    for (unsigned int i = 1; i < Nnodes; i++)
    {
        // first list element memory allocation
        pcur->next = malloc(sizeof(NODE));
        // case it won't work
        if (pcur->next == NULL)
            return NULL;
        // proceed to the next one    
        pcur = pcur->next;
    }
    // last element points to nothing
    pcur->next = NULL;
    // reassign to the first list element
    pcur = ptop;
    // until the list end is reached, 
    // assign parallell-random numbers to each node array 
    do
    {
#pragma omp parallel for
        for (int j = 0; j < N; j++)
          pcur->A[j] = randUint() % USHRT_MAX;
        // proceed to the next list element
        pcur = pcur->next;
    } while (pcur != NULL);

    return (ptop);
}
//***************************************************************
void doSortInList(NODE *top)
{
#pragma omp parallel
    {
        // this section must be run only by the master thread.
#pragma omp master
        {
          while (top)
            {
                // Use the task pragma when you want to identify 
                // a block of code to be executed in parallel 
                // with the code outside the task region. 
                // The task pragma can be useful for parallelizing 
                // irregular algorithms such as pointer 
                // chasing or recursive algorithms.
#pragma omp task firstprivate(top)
                {
                    qsort(top->A, N, sizeof(unsigned short), compar);
                }
              top = top->next;
            }
        }
    }
}
//***************************************************************
int main()
{
#pragma omp threadprivate(seed)
    Top = createLinkList();
    doSortInList(Top);
    return 0;
}