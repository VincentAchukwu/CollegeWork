JMP START
DB 70
ORG 50
DB CF   ; 9
DB FF	; 8
DB 8B	; 7
DB FD	; 6
DB DD	; 5
DB 4F	; 4
DB 9F	; 3
DB B7	; 2
DB 0B	; 1
DB FB	; 0
IN 0

START:
	SUB AL,30
	MOV BL,0
	JMP CHECK

; CHECK BACK AGAIN TO GET IT WORKING
CHECK:
	CMP AL,BL
	JZ SAVE
	INC BL
	CMP BL,A
	JNZ CHECK
	MOV BL,0
	IN 0
	JMP CHECK
	MOV BL,50

SAVE:
	PUSH AL
	POP DL

LOOP:
	STI
	CMP BL,5A
	JZ ENDING
	JMP LOOP

ORG 90
	CLI
	MOV AL,[BL]
	OUT 02
	SUB AL,1
	OUT 2
	INC BL
	IRET

ENDING:
	END