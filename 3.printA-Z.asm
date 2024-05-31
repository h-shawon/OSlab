.model small
.stack 100h
.data

.code 
main proc
    mov cx,26
    mov ah,2
    mov dl,'A'

    L1:
    int 21h
    inc dl
    loop L1

    mov ah,2
    mov dl,10
    int 21h
    
    exit:
    mov ah,4ch
    int 21h
    main endp
end main
