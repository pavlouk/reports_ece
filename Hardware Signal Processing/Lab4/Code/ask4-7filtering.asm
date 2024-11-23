				.def RINT1_R
				.def _entry
				.text
				.ref _coef
				.align 512
buffer_left		.space 512
				.align 512
buffer_right	.space 512
				.align 512
y_buffer_left	.space 512
				.align 512
y_buffer_right	.space 512
				.align 512

IMH_addr		.set 019c0000h
IML_addr		.set 019c0004h
IMH_val			.set 00100000111001100001010010000011b
IML_val			.set 00111101110011010011000001000001b
DRR_ADDR		.set 0x1900000
DXR_ADDR		.set 0x1900004
RCR_ADDR		.set 0x190000C
XCR_ADDR		.set 0x1900010

_entry:			;SET katallila ta IMH IML
				MVKL .S2  IMH_addr,B0 ;IMH_addr => B0
		        MVKH .S2  IMH_addr,B0
		        MVKL .S2  IML_addr,B1 ;IML_addr => B1
		        MVKH .S2  IML_addr,B1
		        MVKL .S2  IMH_val,B2 ;IMH_val => B2
		        MVKH .S2  IMH_val,B2
		        MVKL .S2  IML_val,B3 ;IML_val => B3
		        MVKH .S2  IML_val,B3
		        STW B2,*B0 ;save IMH values to mem
		        STW B3,*B1 ;save IML values to mem
				;enable to INT4-INT15
				MVC IER,B0
				SET B0,1,1,B0 ;set bit 1 of IER (NMI enable)
				SET B0,8,9,B0 ;set bits 8-9 of IER (INT8-9 enable)
				MVC B0,IER
				MVC CSR,B0
				SET B0,0,0,B0 ;set bit 0 of CSR (Global Interrupt Enable)
				MVC B0,CSR
				;clear IFR
				ZERO B0
				SET B0,4,15,B0 ;set bit 4-15 of ICR
				MVC B0,ICR

				MVKL RCR_ADDR,B0 ; RCR_ADDR => B0
				MVKH RCR_ADDR,B0
				MVKL XCR_ADDR,B1 ; XCR_ADDR => B1
				MVKH XCR_ADDR,B1
				MVKL 0x000000A0,B2 ;constant => B2
				MVKH 0x000000A0,B2
				;saves
				STW B2,*B0
				STW B2,*B1
				;buffers_setup
				MVKL buffer_left,A1 ;move left buffer address => A1
				MVKH buffer_left,A1
				MVKL buffer_right,A2 ;move right buffer address => A2
				MVKH buffer_right,A2
				MVKL DRR_ADDR,A3 ;move DRR address => A3
				MVKH DRR_ADDR,A3
				MVK 255,B5 ;gia na elegxoume an exei ftasei sto telos tou buffer (me compare) 512/2=256 halfwords
				MVK 41,B12 ;arithmos coefficient filtrou
				MVKL 0x0000ffff,B2 ;maska gia apofygi lathous otan kanoume OR tou 2 accumulator
				MVKH 0x0000ffff,B2
				;filter buffers klp
				MVKL _coef,A5 ; coefficients pointer => A5
				MVKH _coef,A5
				MVKL y_buffer_left,B14 ;left y buffer => B14
				MVKH y_buffer_left,B14
				MVKL y_buffer_right,B13 ;right y buffer => B13
				MVKH y_buffer_right,B13
				MVKL DXR_ADDR,B3 ;move DXR address => B3
				MVKH DXR_ADDR,B3
				ZERO A15;gia na xrisimopoihthei san counter gia tous x_buffers
				ZERO A4 ;gia na xrisimopoiithei san counter twn syntelestwn gia to eswteriko
				ZERO A6 ;gia na xrisimopoiithei gia counter twn buffer sto eswteriko
				ZERO B9 ;accumulator gia left channel
				ZERO B10;accumulator gia right channel
				ZERO B11;counter gia tous y buffers
;wait for next interrupt
loop:			B loop
				nop 5

;buffer_save
RINT1_R:		LDW	*A3,A0
				nop 4
				STH A0,*A2[A15] ;save 16 LSbits sto right buffer
				nop 4
				SHR A0,16,A0 ;shift right gia na pane ta 16 MSbits stis xamiloteres theseis pou swzei h STH
				STH A0,*A1[A15] ;save 16 LSbits sto right buffer
				MV A15,A6 ;copy iterator to A6 (o A6 krataei th thesi tou pio prosfatou deigmatos stous buffer eisodou)
				;kykliko increment tou iterator twn x_buffer
				;kykliko increment : i = (i + 1)%256
				ADD A15,1,A15 ; counter + 1 (o counter panta metraei posa halfword (2byte) apo tin arxi tou buffer eimaste)
				AND A15,B5,A15 ; mod me 256(dec) == AND me 255(dec) dioti 256 einai dinami tou 2

filter:			LDH *A5[A4],B6 ;load coeff[i] => B6
				LDH *A1[A6],B7 ;load left_buffer[k] => B7
				LDH *A2[A6],B8 ;load right_buffer[k] => B8
				nop 4
				MPY B6,B7,B7 ;coeff * x_left => B7
				MPY B6,B8,B8 ;coeff * x_right => B8
				ADD B7,B9,B9 ;add to left accumulator
				ADD B8,B10,B10 ;add to right accumulator
				ADD A4,1,A4 ;coeff_counter + 1
				;kykliko decrement tou iterator twn x_buffer
				;kykliko decrement : i = (i + 256 - 1)%256
				ADD A6,B5,A6
				AND A6,B5,A6
				CMPEQ A4,B12,B0 ;compare gia na tsekaroume an ftasame sto telos tou filtrou
				[!B0]B filter

				;save_results
				SHR B9,15,B9 ;shift right gia Q15 format
				STH B9,*B14[B11] ;save left accumulator => left y buffer
				SHR B10,15,B10 ;shift right gia Q15 format
				STH B10,*B13[B11] ;save right accumulator => right y buffer
				nop 4
				SHL B9,16,B9 ;fere ta 16 LSbit tou left channel sta MSbit kai ta ypoloipa zero
				AND B2,B10,B10 ;gia na eimaste sigouroi oti ta 16 MSbit tou B10 einai 0
				OR B9,B10,B10 ;or ta 2 channel gia na ftiaksoume to teliko 32bit pou tha grapsoume stin eksodo
				STW B10,*B3 ;save output => DXR
				;kykliko increment tou y_buffer counter
				ADD B11,1,B11
				AND B11,B5,B11
				B IRP
				ZERO B9 ;zero accumulator gia left channel
				ZERO B10 ;zero accumulator gia right channel
				ZERO A4 ;reset coefficient counter
				nop 2
				.end
