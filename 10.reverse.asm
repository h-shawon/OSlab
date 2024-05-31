.MODEL SMALL
.DATA
    MSG DB 0AH,0DH
    OUTPUT DB 0AH,0DH
    NEWLINE DB 0AH,0DH,'$'
    BUF DB 10 DUP('$')

.CODE
MAIN PROC
    MOV AX, @DATA           ; Load data segment address into AX
    MOV DS, AX              ; Initialize data segment register

    MOV AH, 09H             ; DOS function to print string
    LEA DX, MSG             ; Load offset of message string into DX
    INT 21H                 ; Call DOS interrupt

    MOV AH, 0AH             ; DOS function to input string
    LEA DX, BUF             ; Load offset of buffer for input
    INT 21H                 ; Call DOS interrupt

    MOV SI, OFFSET BUF + 2 ; Load offset of input buffer into SI
    CALL REVERSE_STRING     ; Call procedure to reverse the string

    MOV AH, 09H             ; DOS function to print string
    LEA DX, OUTPUT          ; Load offset of output message into DX
    INT 21H                 ; Call DOS interrupt

    MOV DX, OFFSET BUF + 2 ; Load offset of reversed input buffer into DX
    MOV AH, 09H             ; DOS function to print string
    INT 21H                 ; Call DOS interrupt

    MOV AH, 4CH             ; DOS function to terminate program
    INT 21H                 ; Call DOS interrupt

MAIN ENDP

REVERSE_STRING PROC
    XOR CX, CX              ; Clear CX register
    MOV DI, SI              ; Set DI to point to the end of the string
    MOV BX, DI              ; Copy DI to BX for later use

FIND_END:
    CMP BYTE PTR [DI], '$' ; Check if the current character is the end of string
    JE REVERSE              ; If it is, jump to REVERSE
    INC DI                  ; Move DI to the next character
    INC CX                  ; Increment counter
    JMP FIND_END            ; Repeat loop

REVERSE:
    DEC DI                  ; Move DI to the last character before the end of the string
    MOV SI, BX              ; Restore SI to the beginning of the string

REVERSE_LOOP:
    CMP SI, DI              ; Check if SI has crossed DI
    JAE EXIT_REVERSE        ; If it has, jump to EXIT_REVERSE
    MOV AL, [SI]            ; Load character from SI
    MOV AH, [DI]            ; Load character from DI
    MOV [SI], AH            ; Swap characters
    MOV [DI], AL
    INC SI                  ; Move SI forward
    DEC DI                  ; Move DI backward
    JMP REVERSE_LOOP        ; Repeat loop

EXIT_REVERSE:
    RET
REVERSE_STRING ENDP

END MAIN
