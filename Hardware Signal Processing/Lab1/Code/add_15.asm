a		.set 0x1234
b		.set 0x0012
x		.set 0x3

		.def entry
		.text
entry:	MVK .S1 a, A0
		MVK .S1 b, A1
		MVK .S1 x, A3
		MPY .M1 A0, A3, A4
		ADD .L1 A4, A1, A2

		IDLE
		.end
