@R0
D = M
@n
M = D

@i
M = 0

@R1
D = M
@t
M = D

@R2
M = 0

@mul
M = 0 

(LOOP)
    @i
    D = M
    @t
    D = D - M
    @STOP
    D;JEQ // if i > t go to STOP

    @mul
    D = M
    @n
    D = D + M
    @mul
    M = D // mul = mul + n

    @i
    M = M + 1
    @LOOP
    0;JMP

(STOP)
    @mul
    D = M
    @R2
    M = D // RAM[2] = mul

(END)
    @END
    0;JMP