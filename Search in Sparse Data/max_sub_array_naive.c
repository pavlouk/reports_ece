#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 1000

void algo_1(int A[], int length)
{
	int m = 0;
	int S, start_ind = 0, end_ind = 0;

	clock_t t;
	t = clock();

	for (int j = 0; j < length; j++)
	{
		for (int k = j; k < length; k++)
		{
			S = 0;
			for (int i = j; i < k; i++)
				S = S + A[i];
			if (S > m)
			{
				m = S;
				start_ind = j;
				end_ind = k;
			}
		}
	}

	t = clock() - t;
	double time_taken = ((double)t) / CLOCKS_PER_SEC; // in seconds

	printf("starting point: %d ending point: %d \nresult: %d \ntime taken: %f \n", start_ind, end_ind, m, time_taken);
}

int main()
{
	int B[N];
	int C[2 * N];
	srand(1046970);
	for (int i = 0; i < N; i++)
	{
		B[i] = rand() % 20 - 10;
	}
	algo_1(B, N);
	for (int i = 0; i < 2 * N; i++)
	{
		C[i] = rand() % 20 - 10;
	}
	algo_1(C, 2 * N);
	return 0;
}
