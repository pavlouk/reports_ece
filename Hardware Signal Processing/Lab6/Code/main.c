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
void First_2nd(int data);
void Second_2nd(short int wn);
short int Q15_Mult(short int coeff, short int data);
void init_hw_interrupts(void);

short int xn, xn_1 = 0, xn_2 = 0;
short int yn = 0, yn_1 = 0, yn_2 = 0;
short int wn = 0, wn_1 = 0, wn_2 = 0;

// First 2nd class filter parameters
short int b11 = 47860, b21 = 32764;
short int a11 = 22006, a21 = 34648; //a1 use as 2*a1
short int G1 = 13447;
// Second 2nd class filter parameters
short int b12 = 43633, b22 = 16384;
short int a12 = 31188, a22 = 51141;
short int G2 = 24084;

int data;

void main()
{

	DSK6713_init();		// Initialize the board support library, must be called first
	hCodec = DSK6713_AIC23_openCodec(0, &config);	// open codec and get handle
	// set codec sampling frequency 48kHz
	DSK6713_AIC23_setFreq(hCodec, DSK6713_AIC23_FREQ_48KHZ);
	*(unsigned volatile int *)McBSP1_RCR = 0x00A0;
	*(unsigned volatile int *)McBSP1_XCR = 0x00A0;
//	comm_intr();
	init_hw_interrupts();
	while(1);  // wait for interrupts

}

// interrupt service routine
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

	data = input_leftright_sample();
	// "data" contains both audio channels

	// ---------------------- Useful code goes here ----------------------
    First_2nd(data);
    Second_2nd(wn);
    
	int temp = (int)yn;
	temp = temp << 16;
	data = temp | (int) yn;
	// -------------------------------------------------------------------

	// process "data", or pass another variable to change the output
	output_leftright_sample(data);

}

short int Q15_Mult(short int coeff, short int data) {
    int temp;
    short int Q;
    temp = (int)coeff * (int) data;
    Q = (short) temp >> 15;
    return Q;
}

void First_2nd(int data) {
    xn = (short)data;
    
    short int Gb11  = Q15_Mult(G11, b11), Gb21 = Q15_Mult(G11, b21);
    // Calculate the output of the first filter
    wn = (Q15_Mult(2*a11, wn_1)) + (Q15_Mult(a21, wn_2)) + Q15_Mult(G11, xn) + Q15_Mult(Gb11, xn_1) + Q15_Mult(Gb21, xn_2);
    
    wn_2 = wn_1;                                                                // Save current values
    wn_1 = wn;
    
    xn_2 = xn_1;
    xn_1 = xn;
    
}

void Second_2nd(short int wn) {
    short int Gb12  = Q15_Mult(G2, 2 * b12), Gb22 = Q15_Mult(G2,2 * b22);
    // Calculate the output of the second filter
    yn = (Q15_Mult(a12, yn_1)) + (Q15_Mult(a21, yn_2)) + Q15_Mult(G2, wn) + Q15_Mult(Gb12, wn_1) + Q15_Mult(Gb22, wn_2);
    
    yn_2 = yn_1;                                                                // Save current values
    yn_1 = yn;
    
    wn_2 = wn_1;
    wn_1 = wn;
}
