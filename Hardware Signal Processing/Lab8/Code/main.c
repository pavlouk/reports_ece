#include <stdio.h>
#include <c6x.h>
#include <csl.h>
#include <csl_mcbsp.h>
#include <csl_irq.h>
#include "dsk6713.h"
#include "dsk6713_aic23.h"
#include "C6xdsk.h"
#include <math.h>
#include "dsp_bitrev_cplx.h"
#include "dsp_radix2.h"

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
void FFT(short * signal, short * coeff);
void calculate_coeff(short * coeff);
void bitrev_index(short *index, int n);
void abs_val(int * signal, int * amplitude);

short signal[128];
short index[8];
short coeff[64];
int amplitude[64];
int n = 0;

void main()
 {
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
	int data;
	data = input_leftright_sample();
	if (n != 128) {
		signal[n] =  (short)data;
		signal[n + 1] = 0;
	} else {
		n = 0;
		signal[n] = (short)data;
		signal[n + 1] = 0;
		calculate_coeff(coeff);
		FFT(signal, coeff);
		abs_val((int * )signal, amplitude);
	}
	n += 2;

	output_leftright_sample(data);
}

short Q15_Mult(short coeff, short data, int flag) {
    int temp;
    short Q;
    if (flag) (Q = (coeff * (int)data) >> 14);
    else (Q = (coeff * (int)data) >> 15);
    return Q;
}

void FFT(short * signal, short * coeff) {
	DSP_radix2(64, signal, coeff);
	bitrev_index(index, 64);
	DSP_bitrev_cplx((int *)signal, index, 64);

}

void abs_val(int * signal, int * amplitude){
	short real, imag;
	int i;
	for (i = 0; i < 64; i++) {
		imag = signal[i] & 0xFFFF;
		real = (signal[i] >> 16) & 0xFFFF;
		amplitude[i] = (int)(real*real) + (int)(imag*imag);
	}
}

void calculate_coeff(short * coeff){
	int i, nx = 64;
	for (i = 0; i < nx/2; i++) {
		coeff[i*2] = 32767 * (-cos(i*2*PI/nx));
		coeff[i*2 + 1] = 32767 * (-sin(i*2*PI/nx));
	}
}
