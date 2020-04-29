#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 10000

void algo_21(int A[], int length) {
	int S[N + 1] = { 0 };
	int start_ind = 0, end_ind = 0, m = 0;
	int s;

	clock_t t;
	t = clock();

	for (int i = 0; i < length; i++)
		S[i + 1] = S[i] + A[i];

	for (int j = 0; j < length; j++)
	{
		for (int k = j; k < length; k++)
		{
			s = S[k - 1] - S[j];
			if (s > m)
			{
				m = s;
				start_ind = j;
				end_ind = k - 1;
			}
		}
	}

	t = clock() - t;
	double time_taken = ((double)t) / CLOCKS_PER_SEC; // in seconds

	printf("starting point: %d ending point: %d \nresult: %d \ntime taken: %f \n", start_ind, end_ind, m, time_taken);
}

void algo_22(int A[], int length) {
	int S[2*N + 1] = { 0 };
	int start_ind = 0, end_ind = 0, m = 0;
	int s;

	clock_t t;
	t = clock();

	for (int i = 0; i < length; i++)
		S[i + 1] = S[i] + A[i];

	for (int j = 0; j < length; j++)
	{
		for (int k = j; k < length; k++)
		{
			s = S[k - 1] - S[j];
			if (s > m)
			{
				m = s;
				start_ind = j;
				end_ind = k - 1;
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
	int C[2*N];
	srand(1046970);
	for (int i = 0; i < N; i++) {
		B[i] = rand() % 20 - 10;
	}
	algo_21(B, N);
	for (int i = 0; i < 2*N; i++) {
		C[i] = rand() % 20 - 10;
	}
	algo_22(C, 2*N);
	  return 0;
}
