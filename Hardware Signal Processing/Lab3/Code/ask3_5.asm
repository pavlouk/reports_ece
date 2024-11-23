		.def entry
		.def INT4_R
		.text

IMH_pointer	.set 0x019c0000
IML_pointer	.set 0x019c0004
clock_period .set 0x03567E00 	;56million cycles count = 1sec
timer0_cntr .set 0x01940000 	;timer0 control register address
timer0_per .set 0x01940004 		;timer0 period address
timer0_init .set 0x2C1 		    ;timer0 initialization values

;load addresses


entry:	MVKL .S1 IML_pointer, A3
		MVKH .S1 IML_pointer, A3
		MVK  .S1 0X1		, A1
		STH	 .D1 A1			, *A3
		MVKL .S2  0X13, B0 			;First bit of NMI and INT4
		MVC  .S2  B0, IER
		MVKL .S2  1, B1 			;First bit of GIE
		MVC  .S2  B1, CSR
		NOP
		MVKL timer0_cntr,B1 ;timer0control(addr) => B1
		MVKH timer0_cntr,B1
		MVKL timer0_per,B2 ;timer0 period(addr) => B2
		MVKH timer0_per,B2
		MVKL 0x90080000,B10 ;LED Byte Address => B10
		MVKH 0x90080000,B10
;load constants to registers
		MVKL clock_period,B3 ;timer0 period => B3
		MVKH clock_period,B3
		MVK 0x1,B11 ; B11 = 1 gia XOR sto INT4_R
		MV B11,B12 ; B12 = 1 arxika (arxika grafetai sto Led0 na einai ON)
		STB B12,*B10
;initialize timer control registers 0
		ZERO B0
		SET B0,8,9,B0 ;set CLKSRC kai C/P pedio tou timer0 cntrl register
	    STW B3,*B2 ;save period to per_address
		MVK timer0_init,B0
		STW B0,*B1 ;save timer0 initialization values to timer control register
loop:	B loop
		nop 5
INT4_R: XOR B12,B11,B12
		STB B12,*B10
		B IRP
		nop 5
