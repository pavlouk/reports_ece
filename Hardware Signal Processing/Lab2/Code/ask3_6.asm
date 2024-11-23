		.def entry
		.text

entry:	MVKL .S2 0x90080000, B0
		MVKH .S2 0x90080000, B0		; Load the address
		MVK .S2 0x4, B2				; Load bit shifts
		MVK .S2 0x7, B4

loop:	LDW  .D2 *B0, B1			; Load the bit set ( switch & led states)
		NOP 4						; Wait to load
		[B0] B .S2 loop				; Prepare to branch
		SHRU .S2 B1, B2, B3			; Shift right 4 times
		AND .S2 B3, B4, B5
		STB .D2 B5, *B0				; Store states of switches to the states of the LEDs
		NOP 3						; Wait to branch
