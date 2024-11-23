		.def entry
		.text

entry:	MVK .S2 0x0120, B3		; Address of a
		MVK .S2 0xa, B1			; Control value (10)
		MVK .S2 0x1, B2			; Counter
		MVK .S2 0x1, B4			; Increment value
loop:	CMPEQ .L2 B2, B1, B0	; if counter == 10
		[!B0] B .S2 loop		; Prepare to branch in 5 cycles
		STB .D2 B2, *B3++[1]	; Store counter in a  and increase address by 1 byte
		ADD .S2 B2, B4, B2		; Increase counter
		NOP 3					; Remaining cycles
								; Branch!!!

		MVK .S2 0x0120, B3		; Set address to a[0]

		MVK .S2 0x0130, B5		; Address of x
		MVK .S2 0x6, B1			; Control value
		MVKL .S2 0xf, B2
		MVKH .S2 0xf, B2		; Counter
								; Decrement value = 1
loop2:	CMPEQ .L2 B2, B1, B0	; if counter == 6
		[!B0] B .S2 loop2		; Prepare to branch in 5 cycles
		STB .D2 B2, *B5++[1]	; Store counter in x and increase address by 1 byte
		SUB .S2 B2, B4, B2		; Decrease counter
		NOP 3					; Remaining cycles
								; Branch!!!

		MVK .S2 0x0130, B5		; Set address to x[0]

		ZERO B2					; Counter
		MVK .S2 0xa, B1			; Control value
		ZERO B8					; y = 0
loop3:	LDB *B3++[1], B6		; Load a (Will be completed after 4 additional cycles)
		LDB *B5++[1], B7		; Load x (Will be completed after 4 additional cycles)
		ADD .S2 B2, B4, B2		; Increase counter
		NOP 3					; Wait for values a,x to be loaded
		MPY .M2 B6, B7, B6		; Multiply a*x
		nop						; Wait for a8x to be calculated
		ADD .S2 B8, B6, B8		; y = y + a*x
		CMPEQ .L2 B2, B1, B0	; if counter == 10
		[!B0] B .S2 loop3		; Prepare to branch in 5 cycles
		NOP 5					; Wait 5 cycles
								; Branch!!!

		IDLE
		.end
