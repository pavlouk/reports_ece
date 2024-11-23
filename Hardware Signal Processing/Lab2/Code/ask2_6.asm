		.def entry
		.text

entry:	MVK .S2 0x1, B2
		ZERO B1
		MVK .S2 0x64, B0
loop:	[B0] B .S2 loop
		ADD .S2 B1, B0, B1
		SUB .S2 B0, B2, B0
		NOP 3

		IDLE
		.end
