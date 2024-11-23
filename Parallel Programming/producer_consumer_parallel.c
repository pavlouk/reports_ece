#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#define BUFFER_SIZE 30

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

int buff[BUFFER_SIZE];
int last_pos = 0;

//first thread
void *producer(void *arg)
{
	while (1)
	{
		while (last_pos < BUFFER_SIZE)
		{
			sleep(rand() % 2);
			pthread_mutex_lock(&mutex);
			for (int i = 0; i < BUFFER_SIZE; i++)
				printf("%d", buff[i]);
			printf(" producer \n");
			buff[last_pos++] = 1;
			pthread_mutex_unlock(&mutex);
		}
	}
}

//second thread
void *consumer(void *arg)
{
	while (1)
	{
		while (last_pos > 0)
		{
			sleep(rand() % 2);
			pthread_mutex_lock(&mutex);
			buff[--last_pos] = 0;
			for (int i = 0; i < BUFFER_SIZE; i++)
				printf("%d", buff[i]);
			printf(" consumer \n");
			pthread_mutex_unlock(&mutex);
		}
	}
}

int main()
{
	pthread_t prod;
	pthread_t con;

	pthread_create(&prod, NULL, producer, NULL);
	pthread_create(&con, NULL, consumer, NULL);

	pthread_join(&prod, NULL);
	pthread_join(&con, NULL);
	return 0;
}
