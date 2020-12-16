; some good things here, but incomplete.
; some confusion about interupts. Timer one was good, but
; keyboard one had issues.
; overall good attempt.
; Q3.asm
; Enter your name here: Vincent Achukwu
; Enter your ID here: 17393546


; Code goes below this point.

; I noticed how it adds an extra space after getting input from keyboard,
; not sure if that's okay
; unfortunately did't have time in the end to fix it.

JMP START
DB 70			; HANDLE TIMER INTERRUPT
; didn't need this simple keyboard was required.
DB A0			; HANDLE KEY BOARD INTERRUPT

ORG 50
DB 23			; ASCII FOR #
DB 20			; ASCII FOR SPACE

START:
	MOV AL,50	; POINTER TO HAS/SPACE VALUES
	MOV BL,C0	; POINTER/CURSOR FOR VDU
LOOP:
	STI		; START INTERRUPTS
	CMP BL,0	; CHECK IF WE REACHED END OF VDU
	JZ FINISHED	; IF SO, WE FINISH
	JMP LOOP	; JMP LOOP

ORG A0			; THIS HANDLES KEYBOARD INTERRUPT
; so here you should have disabled interrupts, and not used IN
PUSH AL			; SAVES WHAT AL WAS
IN 0			; GET INPUT AND STORE INTO DL
PUSH AL
POP DL
MOV [BL],DL		; STORE INTO VDU
POP AL
CMP AL,50		; CHECK IF WE ADDED # OR SPACE INTO VDU
JZ TO_HASH1		; IF #, WE SWAP TO SPACE AND VICE VERSA
TO_SPACE1:
	INC AL
TO_HASH1:
	DEC AL
INC BL
JMP KEY


ORG 70
CLI			; CLOSES INTERRUPTS
KEY:
;	PUSH AL
;	IN 0
;	PUSH AL
;	POP DL
;	MOV [BL],DL
;	POP AL
MOV CL,[AL]
MOV [BL],CL		; ADDS # OR SPACE TO VDU
INC BL
CALL 7C			; CALLS PROCEDURE TO HANDLE BETWEEN SPACE AND INTERRUPTS
IRET

CMP CL,23
JZ TO_HASH

TO_SPACE:
	INC AL
	RET

TO_HASH:
	DEC AL
	RET

FINISHED:
	END