/*****************************************************************************
* FILENAME
*   Delays and echo.c
*
* DESCRIPTION
*   Delays and Echo using TMS320C6713 DSK Board and AIC23 audio codec.
*   Based on sampling rate of 48000 samples per second. Delay up to 4 seconds.  */
/*********************************************************************************/

#include <stdio.h>
#include "bargraph.h"
#include "stereo.h"
#include "switches.h"
#include "c6713dsk.h"
#include "dsk6713_aic23.h"
#include "stdlib.h"
#include "math.h"

#define N (48000 * 4)


// Codec configuration settings
DSK6713_AIC23_Config config = { \
	0x0017,  /* 0 DSK6713_AIC23_LEFTINVOL  Left line input channel volume */ \
	0x0017,  /* 1 DSK6713_AIC23_RIGHTINVOL Right line input channel volume */\
	0x01f9,  /* 2 DSK6713_AIC23_LEFTHPVOL  Left channel headphone volume */  \
	0x01f9,  /* 3 DSK6713_AIC23_RIGHTHPVOL Right channel headphone volume */ \
	0x0015,  /* 4 DSK6713_AIC23_ANAPATH    Analog audio path control */      \
	0x0000,  /* 5 DSK6713_AIC23_DIGPATH    Digital audio path control */     \
	0x0000,  /* 6 DSK6713_AIC23_POWERDOWN  Power down control */             \
	0x0043,  /* 7 DSK6713_AIC23_DIGIF      Digital audio interface format */ \
	0x0001,  /* 8 DSK6713_AIC23_SAMPLERATE Sample rate control */            \
	0x0001   /* 9 DSK6713_AIC23_DIGACT     Digital interface activation */   \
};

void switch_status_display(int status);
float get_delay_time(int delay);
unsigned int delayed_input(float time, int position, int *buffer);
void delay_array_clear(signed int *BUFFER);
far signed int delay_array[N]; /* Buffer for maximum delay of 4 seconds */

/*
 Uses DIP switches to control the delay time between 0 ms and
 4 seconds. 48000 samples represent 1 second.
*/

float get_delay_time(int delay) {
	float time;
	time = delay*4.0f/7.0f;
	return(time);
}

/*
Take oldest sample from the array and replace with the newest
Uses a circular buffer because a straight buffer would be too slow.
*/

unsigned int delayed_input(float time, int position, int *buffer) {

unsigned int echo;
int displacement, pos;
displacement = time * 48000;

if (displacement == 0) {
	echo = buffer[position];
} else {
	if (displacement > position) {
		pos = N - displacement + position;
		echo = buffer[pos];
	} else {
		pos = position - displacement;
		echo = buffer[pos];
	}
}
echo = (short)(echo >> 16);
return echo;
}


/*
Fill delay array with zeroes to prevent noise / clicks.
*/

void delay_array_clear(signed int *BUFFER){
	int i;
	for (i = 0; i < N; i++) {
		BUFFER[i] = 0;
	}
}

/*
Show status on Stdout window.
*/

void switch_status_display(int status) {
	printf("Present state is: %d\n", status);
}


int main(void)
{
	DSK6713_AIC23_CodecHandle hCodec;
	unsigned int val, newEcho, oldEcho;
	int position = 0;
	short int status, prevStatus = 0;
	float time;
	// Initialize BSL
	DSK6713_init();

	//Start codec
	hCodec = DSK6713_AIC23_openCodec(0, &config);

	// Set  frequency to 48KHz
	DSK6713_AIC23_setFreq(hCodec, DSK6713_AIC23_FREQ_48KHZ);

//------------------------------------------------------------------------------------------
//                            Enter the appropriate code here
//------------------------------------------------------------------------------------------

* (unsigned volatile int*) McBSP1_RCR = 0x000000A0;
* (unsigned volatile int*) McBSP1_XCR = 0x000000A0;

delay_array_clear(delay_array);
while(1) {
	while(!DSK6713_AIC23_read(hCodec, &val));
	delay_array[position] = val;
	newEcho = val & 0xffff0000;
	status = user_switches_read();
	status = 7 - status;
	prevStatus = prevStatus - status;
	if (prevStatus != 0)
		switch_status_display(status);
	prevStatus = status;
	time = get_delay_time(status);
	oldEcho = delayed_input(time, position, delay_array);
	val =newEcho + oldEcho;
	position++;
	position = position % N;
	while(!DSK6713_AIC23_write(hCodec, val));
}
//------------------------------------------------------------------------------------------
	return (0);
}
