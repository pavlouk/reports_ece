RCR				.set	0x190000C
XCR				.set	0x1900010
enable_value	.set	0x000000A0

			.def _entry
			.text

_entry:		MVKL .S1 RCR, A0
			MVKH .S1 RCR, A0
			MVKL .S1 XCR, A1
			MVKH .S1 XCR, A1
			MVKL .S1 enable_value, A2
			MVKH .S1 enable_value, A2
			STW  .D1 A2, *A0
			STW  .D1 A2, *A1

			.end
