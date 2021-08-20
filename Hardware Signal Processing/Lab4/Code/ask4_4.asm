DRR 		.set 0x1900000
DXR			.set 0x1900004
SPCR		.set 0x1900008

			.def _entry
			.text

_entry:		MVKL .S1 DRR, A0
			MVKH .S1 DRR, A0
			MVKL .S1 DXR, A1
			MVKH .S1 DXR, A1
			MVKL .S1 SPCR, A2
			MVKH .S1 SPCR, A2
			MVKL .S1 0x10000, A3
			MVKH .S1 0x10000, A3
			MVK  .S2 0x1, B2

loopa:		LDW *A2, B0
			NOP 4
			AND B0, B2, B0 ;Isolating first bit
			XOR B0, B2, B0 ;Xor logic for inverting
   			[B0] B loopa
  			NOP 5
			LDW *A0, A4  	;Reading input
  			NOP 4

loopb:  	LDW *A2, B1
			NOP 4
			AND B1, A3, B1  ;Isolating 17th bit
			XOR B1, A3, B1  ;Xor logic for inverting
   			[B1] B loopb
			NOP 5
       	    STW .D1	A4, *A1   ;Storing input
			B loopa
			NOP 5

 			IDLE
        	.end
