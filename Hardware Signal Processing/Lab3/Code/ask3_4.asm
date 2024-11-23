	.def entry
	.text

entry:	MVKL .S2 0xFFFF, B2
		MVKH .S2 0xFFFF, B2
		MVC  .S2 B2	   , ICR 	;Set 1 for every interrupt
		IDLE
		.end
