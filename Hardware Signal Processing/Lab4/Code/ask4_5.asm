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

_entry:		MVKL .S1 RCR, A0
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
			MVKL .S1 DRR, A0
			MVKH .S1 DRR, A0
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
			MVKL .S2  0x1, B1 			;First bit of GIE
			;MVC  .S2  B1, CSR
			NOP

loopa:		B loopa
			MVC  .S2  B1, CSR
  			NOP 4
INT4_R:		LDW *A0, A4  	;Reading input
  			NOP 4

		    STW .D1	A4, *A1   ;Storing input
			B loopa
			NOP 5

 			IDLE
        	.end
