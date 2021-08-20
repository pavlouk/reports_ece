		.def entry
		.text

entry:	MVK .S1 0x1234, A0
		MVK .S1 0x0012, A1
		ADD .L1 A0, A1, A2
		IDLE
		.end
