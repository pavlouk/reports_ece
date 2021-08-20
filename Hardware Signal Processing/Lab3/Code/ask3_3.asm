	.def entry
	.text

entry:	MVKL .S2  0X13, B0 			;First bit of NMI and INT4
		MVC  .S2  B0, IER
		MVKL .S2  1, B1 			;First bit of GIE
		MVC  .S2  B1, CSR
		NOP
		IDLE

		.end
