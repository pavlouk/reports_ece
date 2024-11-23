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

buffer_left  .space 512
buffer_right .space 512

_entry:		MVKL .S1 buffer_right, A8
			MVKH .S1 buffer_right, A8
			MVKL .S1 buffer_left, A9
			MVKH .S1 buffer_left, A9
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
			STW	 .D1 A6, *A5			; load the interrupts in IML
			MVKL .S1 DRR, A10
			MVKH .S1 DRR, A10
			MVKL .S1 DXR, A1
			MVKH .S1 DXR, A1
			MVKL .S1 SPCR, A2
			MVKH .S1 SPCR, A2
			MVKL .S1 0x10000, A3
			MVKH .S1 0x10000, A3
			MVK  .S2 0x1, B2

			;enable the interrupts

			MVKL .S2  0X403, B0 			;First bit of NMI and INT10
			MVC  .S2  B0, IER
			MVKL .S2  0x1, B2 			;First bit of GIE
			NOP

loopb:		MVKL .S2 0x1FF, B1
			MVKH .S2 0x1FF, B1

loopa:		B loopa
			MVC  .S2  B2, CSR
  			NOP 4
INT4_R:		LDW *A10, A4  	;Reading input
			NOP 4
			MV .L1 A4, A11
  			STH .D1 A4, *A8++
  			SHR .S1 A4,0x10, A7
  			STH .D1 A7,*A9++
  			SUB .D2 B1, B2, B1
  			[!B1] B loopb

		    STW .D1	A11, *A1   ;Storing input
			B loopa
			NOP 5

 			IDLE
        	.end
