IMH_pointer	.set 0x019c0000
IML_pointer	.set 0x019c0004

		.def entry
		.text

entry:	MVKL .S1 IML_pointer, A3
		MVKH .S1 IML_pointer, A3
		MVKL .S1 IMH_pointer, A2
		MVKH .S1 IMH_pointer, A2
		MVK  .S1 0X3DCD		, A0
		MVK  .S1 0X3041		, A1
		STH	 .D1 A1			, *A3++[1]
		STH	 .D1 A0			, *A3

 		IDLE
 		.end
