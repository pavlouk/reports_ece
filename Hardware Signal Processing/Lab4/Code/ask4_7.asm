		.align 2
output  .space 512
buffer_right .space 512
DRR 		.set 0x1900000
DXR			.set 0x1900004
SPCR		.set 0x1900008
RCR			.set	0x190000C
XCR			.set	0x1900010
enable_value	.set	0x000000A0
IMH_VALUE	.set 0xF
IMH_pointer	.set 0x019c0000

			.def INT4_R
			.def _entry
			.text

_entry:		MVKL .S1 buffer_right, A8
			MVKH .S1 buffer_right, A8
			MVKL .S1 output, A3
			MVKH .S1 output, A3
			MVKL .S1 RCR, A0
			MVKH .S1 RCR, A0
			MVKL .S1 XCR, A1
			MVKH .S1 XCR, A1
			MVKL .S1 enable_value, A2
			MVKH .S1 enable_value, A2
			STW  .D1 A2, *A0
			STW  .D1 A2, *A1
			MVKL .S1 IMH_pointer, A5
			MVKH .S1 IMH_pointer, A5
			MVKL .S1 IMH_VALUE, A6
			MVKH .S1 IMH_VALUE, A6
			STW	 .D1 A6, *A5			;load the interrupts in IML
			MVKL .S1 DRR, A10
			MVKH .S1 DRR, A10
			MVKL .S1 DXR, A1
			MVKH .S1 DXR, A1
			MVKL .S1 SPCR, A2
			MVKH .S1 SPCR, A2
			MVKL .S1 0x100, B1   ;Counter of 256 init
			MVKH .S1 0x100, B1
			MVK  .S2 0x1, B2	;Decrementor

			;enable the interrupts

			MVKL .S2  0X403, B0 	;First bit of NMI and INT10
			MVC  .S2  B0, IER
			MVKL .S2  0x1, B2 		;First bit of GIE
			NOP


loopa:		B loopa
			MVC  .S2  B2, CSR
  			NOP 4


INT4_R:		[!B1] B buff_full  ;check if buff is full
			NOP 5
			LDW *A10, A4  	;Reading input
			MV .L1 A8, A11  ;Storing the buffer start
  			STH .D1 A4, *A8++ ;storing in buffer
  			SUB .D2 B1, B2, B1  ;Decrement of counter 256
  			MVKL .S1 _coef, A14
			MVKH .S1 _coef, A14
		    ZERO A7 	;Total sum of the sample
		    MVK 0x29, B0  ; 41 elements

filter:		LDH *A11--, A
			LDH *A11++, A
			SUB


buff_full:	MVKL .S1 buffer_right, A8 ;pointer at buffer start
			MVKH .S1 buffer_right, A8
			MVKL .S1 output, A3 	  ;pointer at output start
			MVKH .S1 output, A3
			MVKL .S2 0x100, B1		;Counter of 256
			MVKH .S2 0x100, B1
			B INT4_R
			NOP 5

 			IDLE
        	.end
