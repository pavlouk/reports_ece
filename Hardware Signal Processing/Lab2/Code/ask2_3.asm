		.def entry
		.text
entry:	MVKL .S1 0x00000124, A0
		MVKH .S1 0x00000124, A0
		MVKL .S1 0x53fe23e4, A10
		MVKH .S1 0x53fe23e4, A10
		STW  .D1 A10, *A0

		IDLE
		.end
