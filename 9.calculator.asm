.MODEL SMALL
.STACK 100H
.DATA  

MSG1 DB 10,13,'1.Add$'
MSG2 DB 10,13,'2.Sub$'
MSG3 DB 10,13,'3.Mul$'
MSG4 DB 10,13,'4.Div$'
MSG5 DB 10,13,'Choose One:$'
MSG6 DB 10,13,10,13,'Enter 1st Number:$'
MSG7 DB 10,13,'Enter 2nd Number:$'
MSG8 DB 10,13,10,13,'The Result is:$' 


NUM1 DB ?
NUM2 DB ?
RESULT DB ?
.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX 
    
    LEA DX,MSG1
    MOV AH,9
    INT 21H
    
    LEA DX,MSG2
    MOV AH,9
    INT 21H
    
    LEA DX,MSG3
    MOV AH,9
    INT 21H
    
    LEA DX,MSG4
    MOV AH,9
    INT 21H 
    
    
    
    LEA DX,MSG5
    MOV AH,9
    INT 21H
    
  
    MOV AH,1
    INT 21H
    MOV BH,AL
    SUB BH,48
    
    CMP BH,1
    JE ADD
    
    CMP BH,2
    JE SUB

    CMP BH,3
    JE MUL
    
    CMP BH,4
    ;JE DIV
    
    
  ADD:
    LEA DX,MSG6  ;ENTER 1ST NUMBER
    MOV AH,9
    INT 21H 
    
    MOV AH,1
    INT 21H
    MOV BL,AL
    
    LEA DX,MSG7    ;ENTER 2ND NUMBER
    MOV AH,9
    INT 21H 
    
    MOV AH,1
    INT 21H
    MOV CL,AL
    
    ADD AL,BL
    MOV AH,0
    AAA
    
    
    MOV BX,AX 
    ADD BH,48
    ADD BL,48 
    
    LEA DX,MSG8
    MOV AH,9
    INT 21H
    
    
    MOV AH,2
    MOV DL,BH
    INT 21H
    
    MOV AH,2
    MOV DL,BL
    INT 21H
    
    
  SUB:

    LEA DX,MSG6  ;ENTER 1ST NUMBER
    MOV AH,9
    INT 21H 
    
    MOV AH,1
    INT 21H
    MOV BL,AL
    
    LEA DX,MSG7    ;ENTER 2ND NUMBER
    MOV AH,9
    INT 21H 
    
    MOV AH,1
    INT 21H
    MOV CL,AL
    
    SUB BL,CL
    ADD BL,48
    
    LEA DX,MSG8
    MOV AH,9
    INT 21H
    
    
    MOV AH,2
    MOV DL,BL
    INT 21H
    
  MUL:

    LEA DX,MSG6
    MOV AH,9
    INT 21H
    
    
    MOV AH,1
    INT 21H
    SUB AL,30H
    MOV NUM1,AL
    
    
    LEA DX,MSG7
    MOV AH,9
    INT 21H 
    
    
    MOV AH,1
    INT 21H
    SUB AL,30H
    MOV NUM2,AL
    
    
    MUL NUM1
    MOV RESULT,AL
    AAM  
    
    
    ADD AH,30H
    ADD AL,30H
    
    
    MOV BX,AX 
    
    
    LEA DX,MSG8
    MOV AH,9
    INT 21H 
    
    MOV AH,2
    MOV DL,BH
    INT 21H
    
    MOV AH,2
    MOV DL,BL
    INT 21H
   
   DIV:
    LEA DX,MSG6
    MOV AH,9
    INT 21H
    
    
    MOV AH,1
    INT 21H
    SUB AL,30H
    MOV NUM1,AL
    
    
    LEA DX,MSG7
    MOV AH,9
    INT 21H 
    
    
    MOV AH,1
    INT 21H
    SUB AL,30H
    MOV NUM2,AL
    
    MOV CL,NUM1
    MOV CH,00
    MOV AX,CX  
    
    DIV NUM2
    MOV RESULT,AL
    MOV AH, 00
    AAD  
    
    
    ADD AH,30H
    ADD AL,30H
    
    
    MOV BX,AX 
    
    
    LEA DX,MSG8
    MOV AH,9
    INT 21H 
    
    MOV AH,2
    MOV DL,BH
    INT 21H
    
    MOV AH,2
    MOV DL,BL
    INT 21H
  
    EXIT:
    
    MOV AH,4CH
    INT 21H
    MAIN ENDP
END MAIN