        	.title  "vectors.asm"
			.ref	_c_int00
			.ref 	INT4_R
			.ref 	INT5_R

        	.sect 	"vectors"

rst:    	MVKL	.S2	_c_int00,B0
       		MVKH	.S2	_c_int00,B0
        	B		.S2	B0
        	nop
        	nop
        	nop
        	nop
        	nop

NMI:		nop
			nop
			nop
			nop
			nop
			nop
        	nop
        	nop


TINT0_ISR:	nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

TINT1_ISR:	nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

RINT1:		MVKL	.S2	INT4_R,B0
       		MVKH	.S2	INT4_R,B0
        	B		.S2	B0
        	nop
        	nop
        	nop
        	nop
        	nop

XINT1:		MVKL	.S2	INT5_R,B0
       		MVKH	.S2	INT5_R,B0
        	B		.S2	B0
        	nop
        	nop
        	nop
        	nop
        	nop

GPINT5_ISR:	nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

GPINT6_ISR:	nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

GPINT7_ISR:	nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

EDMAINT_ISR: nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

EMUDTDMA_ISR: nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

EMURTDXRX_ISR: nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

EMURTDXTX_ISR: nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

XINT0_ISR:	  nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

RINT0_ISR:	  nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop

XINT1_ISR:	   nop
			nop
			nop
        	nop
        	nop
        	nop
        	nop
        	nop




