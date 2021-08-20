        	.title  "vectors.asm"

        	.ref 	entry
        	.ref	INT4_R

        	.sect 	"vectors"

rst:    	MVKL	.S2	entry, B0
       		MVKH	.S2	entry, B0
        	B		.S2	B0
        	nop
        	nop
        	nop
        	nop
        	nop

DSPINT_ISR:	nop
			nop
			nop
			nop
			nop
			nop
        	nop
        	nop

      		nop
			nop
			nop
			nop
			nop
			nop
        	nop
        	nop
        	nop
			nop
			nop
			nop
			nop
			nop
        	nop
        	nop

TINT0_ISR:	MVKL	.S2	INT4_R, B0
       		MVKH	.S2	INT4_R, B0
        	B		.S2	B0
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

SDINT_ISR:	NOP 8

GPINT4_ISR:	NOP 8

GPINT5_ISR:	NOP 8

GPINT6_ISR:	NOP 8

GPINT7_ISR:	NOP 8

EDMAINT_ISR: NOP 8

EMUDTDMA_ISR: NOP 8

EMURTDXRX_ISR: NOP 8

EMURTDXTX_ISR: NOP 8

XINT0_ISR:	   NOP 8

RINT0_ISR:	  NOP 8

XINT1_ISR:	   NOP 8

RINT1_ISR:	  NOP 8



