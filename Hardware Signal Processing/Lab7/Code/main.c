#include <stdio.h>
#include <c6x.h>
#include <csl.h>
#include <csl_mcbsp.h>
#include <csl_irq.h>
#include "dsk6713.h"
#include "dsk6713_aic23.h"
#include "C6xdsk.h"

static DSK6713_AIC23_CodecHandle hCodec;							// Codec handle
static DSK6713_AIC23_Config config = { \
		0x0017,  /* 0 DSK6713_AIC23_LEFTINVOL  Left line input channel volume */ \
		0x0017,  /* 1 DSK6713_AIC23_RIGHTINVOL Right line input channel volume */\
		0x01f9,  /* 2 DSK6713_AIC23_LEFTHPVOL  Left channel headphone volume */  \
		0x01f9,  /* 3 DSK6713_AIC23_RIGHTHPVOL Right channel headphone volume */ \
		0x0011,  /* 4 DSK6713_AIC23_ANAPATH    Analog audio path control */      \
		0x0000,  /* 5 DSK6713_AIC23_DIGPATH    Digital audio path control */     \
		0x0000,  /* 6 DSK6713_AIC23_POWERDOWN  Power down control */             \
		0x0043,  /* 7 DSK6713_AIC23_DIGIF      Digital audio interface format */ \
		0x0001,  /* 8 DSK6713_AIC23_SAMPLERATE Sample rate control */            \
		0x0001   /* 9 DSK6713_AIC23_DIGACT     Digital interface activation */   \
	};  // Codec configuration with default settings

interrupt void serial_port_rcv_isr(void);
short Q15_Mult(short coeff, short data, int flag);
void init_hw_interrupts(void);
short Goertzel(short coef, short* input, int flag);
int max_pos(short* buff);


// Coefficients

short CoeffLow[4] = {0x6D02, 0x68AD, 0x63FC, 0x5EE7};
short CoeffHigh[4] = {0x4A70, 0x4090, 0x6521, 0x479C};
short FreqLow[4] = {697, 770, 852, 941};
short FreqHigh[4] = {1209, 1336, 1477, 1633};
char previous;

char Symbols[4][4] = {
		{'1', '2', '3', 'A'},
		{'4', '5', '6', 'B'},
		{'7', '8', '9', 'C'},
		{'*', '0', '#', 'D'}};

// Define the buffer

short BufferData[205];
int n = 0;

// Define the spectrum matrices

short SpecLow[4] = {0, 0, 0, 0};
short SpecHigh[4] = {0, 0, 0, 0};





void main()
{
	printf("gdgdgd\n");
	DSK6713_init();		// Initialize the board support library, must be called first
	hCodec = DSK6713_AIC23_openCodec(0, &config);	// open codec and get handle
	// set codec sampling frequency at 8kHz
	DSK6713_AIC23_setFreq(hCodec, DSK6713_AIC23_FREQ_8KHZ);
	*(unsigned volatile int *)McBSP1_RCR = 0x00A0;
	*(unsigned volatile int *)McBSP1_XCR = 0x00A0;
//	comm_intr();
	init_hw_interrupts();
	while(1);  // wait for interrupts

}

// interrupt service routine
// Unterbrechung
void init_hw_interrupts(void)
{

	IRQ_globalDisable();			// Globally disables interrupts
	IRQ_nmiEnable();				// Enables the NMI interrupt

	// Maps an event to a physical interrupt
	// We can set the interrupt number wherever we like in vectors.asm ( this is the interrupt number )
	// Interrupt number is the second argument in IRQ_map define
	// The first argument must be set to a physical event and here we use the mcbsp1
	// and we want the receive interrupt so we have RINT1
	IRQ_map(IRQ_EVT_RINT1, 11);
	IRQ_enable(IRQ_EVT_RINT1);		// Enables the event
	IRQ_globalEnable();				// Globally enables interrupts

}

// interrupt service routine
interrupt void serial_port_rcv_isr()
{
	int i;
	int flag = 1;
	int data;
	data = input_leftright_sample();
	int posLow, posHigh;

	n++;
	if (n < 205) {
		BufferData[n-1] = (short)data;
	} else {
		n = 0;
		for (i = 0; i < 4; i++) {
			SpecLow[i] = Goertzel(CoeffLow[i], BufferData, 1);
			if (i == 2 || i == 3) flag = 0;
			SpecHigh[i] = Goertzel(CoeffHigh[i], BufferData, flag);
		}
		posLow = max_pos(SpecLow);
		posHigh = max_pos(SpecHigh);
		if (previous != Symbols[posLow][posHigh]) {
			printf("The character is: %c\n", Symbols[posLow][posHigh]);
			previous = Symbols[posLow][posHigh];
		}
	}
	output_leftright_sample(data);
}

short Q15_Mult(short coeff, short data, int flag) {
    int temp;
    short Q;
    if (flag) (Q = (coeff * (int)data) >> 14);
    else (Q = (coeff * (int)data) >> 15);
    return Q;
}

short Goertzel(short coef, short* input, int flag) {
	short spectrum, t;
	int i;
	short Qn;
	short Qn_1 = 0, Qn_2 = 0;
	for(i = 0; i < 205; i++) {
		Qn = input[i] + Q15_Mult(coef, Qn_1, flag) - Qn_2;
		Qn_2 = Qn_1;
		Qn_1 = Qn;
	}
	t = Q15_Mult(coef, Qn, flag);
	spectrum = Q15_Mult(Qn, Qn, 0) + Q15_Mult(Qn_1, Qn_1, 0) - Q15_Mult(Qn_1, t, 0);
	return spectrum;
}

int max_pos(short* buff) {
	int Pos_max = 0;
	int i;
	short int m = -1;
	for(i = 0; i < 4; i++) {
		if(buff[i] > m) {
			m = buff[i];
			Pos_max = i;
		}
	}
	return Pos_max;
}
