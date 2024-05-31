.model small
.stack 100h
.data 
.code
main proc 
    mov ah,1
    int 21h
    mov bl, al
    int 21h
    mov bh, al
    int 21h
    mov cl,al
    
    mov ah,2
    mov dl,10
    int 21h

    cmp bl, bh

    Jl lebel1 
    Jge lebel2

    lebel1:
        cmp bh,cl
        Jg out1
        Jmp out2
        out1:
            mov ah,2
            mov dl,bh
            int 21h
            Jmp exit
        out2:
            mov ah,2
            mov dl,cl
            int 21h
            Jmp exit
            
    lebel2:
        cmp bl,cl
        Jg out3
        Jmp out4
        out3:
            mov ah,2
            mov dl,bl
            int 21h
            Jmp exit
        out4:
            mov ah,2
            mov dl,cl
            int 21h
            Jmp exit
    exit:
        mov ah,4ch
        int 21h
        main endp
    
    end main