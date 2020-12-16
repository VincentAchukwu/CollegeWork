;	question 1
MOV	CL,20		; Moves 14 into cl (which is 20 in decimal)
LOOP:			; loop starts here
	DEC CL		; decrement cl
	JNZ LOOP	; jumps to loop while zero flag is not set
	JMP NEG		; once zero flag set, jump to neg loop

NEG:
	DEC CL		; decrement cl
	JNS NEG		; jump to neg loop while sign bit not set
	JMP NEXT	; once set, jump to next loop

NEXT:
	DEC CL		;basically decrements once more
	END		; did it like this to show how loops work.....

;====================================================================