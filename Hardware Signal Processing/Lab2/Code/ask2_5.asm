		.def entry
		.text

entry:	MVKL .S1 0x0000ef35, A0
		MVKH .S1 0x0000ef35, A0
		MVK  .S1 0x000033dc, A1
		MVK  .S1 0x00001234, A2
		MVK  .S1 0x00000007, A3
		ADD  .S1 A0, A1, A1
		SUB  .S1 A1, A2, A2
		MPY  .M1 A2, A3, A3
		nop

		IDLE
		.end
