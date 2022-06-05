#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 100000
#define MAX(x, y) (((x) > (y)) ? (x) : (y))

void algo_31(int A[], int length) {
	int M[N + 1] = { 0 };
	int m = 0, start_ind = 0, end_ind = 0;

	clock_t t;
	t = clock();

	for (int t = 0; t < length; t++)
		M[t + 1] = MAX(0, (M[t] + A[t]));

	for (int t = 0; t <= length; t++)
		m = MAX(m, M[t]);

	t = clock() - t;
	double time_taken = ((double)t) / CLOCKS_PER_SEC; // in seconds

	printf("starting point: %d ending point: %d \nresult: %d \ntime taken: %f \n", start_ind, end_ind, m, time_taken);
}

void algo_32(int A[], int length) {
	int M[2*N + 1] = { 0 };
	int m = 0, start_ind = 0, end_ind = 0;

	clock_t t;
	t = clock();

	for (int t = 0; t < length; t++)
		M[t + 1] = MAX(0, (M[t] + A[t]));

	for (int t = 0; t <= length; t++)
		m = MAX(m, M[t]);

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
	algo_31(B, N);
	for (int i = 0; i < 2*N; i++) {
		C[i] = rand() % 20 - 10;
	}
	algo_32(C, 2*N);
}
