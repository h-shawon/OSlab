.model small
.stack 100h
.data

.code 
main proc
    mov cx,9
    mov ah,2
    mov dl,1
    add dl,48
    
    L1:
    int 21h
    inc dl
    loop L1

    mov ah,2
    mov dl,1
    add dl,48
    int 21h

    mov ah,2
    dec dl
    int 21h

    mov ah,2
    mov dl,10
    int 21h
    
    exit:
    mov ah,4ch
    int 21h
    main endp
end main
