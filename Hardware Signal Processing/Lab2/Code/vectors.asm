        .title  "vectors.asm"

        .ref 	entry

        .sect 	"vectors"

rst:    MVKL	.S2	entry, B0
        MVKH	.S2	entry, B0
        B		.S2	B0
        nop		
        nop
        nop
        nop
        nop
