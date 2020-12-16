; This is really excellent.
; Q1.asm
; Enter your name here: Vincent Achukwu
; Enter your ID here: 17393546

; Code goes below this point.

ORG 60
DB "1234564748973849"		; RANDOM VALUES IN DL
DB 20				; END MARKER

ORG 0
MOV AL,60			; START INDEX OF "LIST" OF VALUES
PUSH AL				; SAVE AL

RANGE:				; WE'RE LOOKING FOR BL TO BE END INDEX
	MOV BL,[AL]		; MOVES VALUE IN MEMORY ADDRESS [AL] TO BL
	CMP BL,20		; IF WE REACHED END, WE FOUND END OF "LIST"
	JZ SET_LIMIT
	INC AL			; ELSE KEEP SEARCHING
	JMP RANGE

SET_LIMIT:			; SETS AL <= BL
	PUSH AL
	POP BL
	POP AL

LOOP:
	CALL 1B			; CALLS PROCEDURE AT 1B
	JMP LOOP

MOV DL,[AL]			; DL WILL STORE CURRENT VALUE
SUB DL,30			; CONVERT FROM ASCII
PUSH DL				; SAVE DL
INC AL				; INCREMENT AL (ACTING AS AN INDEX)
CMP CL,DL			; CHECKS WHICH IS BIGGER
JS UPDATE_CL			; IF DL IS BIGGER WE UPDATE CL SINCE SIGN FLAG IS SET

CONTINUE:			; ELSE WE POP DL SO WE CAN RET BACK TO LOOP
	POP DL
	CMP AL,BL		; CHECK IF WE REACHED END OF "LIST" OF NUMBERS
	JZ FINISHED		; IF SO, WE FINISH
	RET			; ELSE RETURN
UPDATE_CL:
	POP CL			; CL BECOMES NEW MAX
	CMP AL,BL
	JZ FINISHED
	RET

FINISHED:
	END