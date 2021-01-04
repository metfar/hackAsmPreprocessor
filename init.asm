(INIT)	// Initialize Intel-try-to-be-compatible simulated registers

@AX		// Accumulator Register	( it is AX=(AH<<8)+AL )				16
M=0		// set to 0

@CX		// Counter Register											17
M=0		// set to 0

@DX		// Data Register											18
M=0		// set to 0

@BX		// Base register											19
M=0		// set to 0

@SI		// Source Index	(I plan use it to store a IP/PC value)		20
M=0		// To return from a GOSUB (go to MMM and come back here)

(START)	// Just the start of the program


		// Macro definitions

//NOP
0; // 1110101010000000		Do nothing but to loose one runtime cycle


// LET VAR=VALUE
@VAR2					// can be replaced by a number
D=A
@VAR1					// this is Address of the variable
M=D


// MOV VAR1,VAR2
@VAR2					// value will be replaced by a number
D=A
@VAR1					// this is Address of the variable
M=D


// MOV VAR1,[MEMORY]
@MEMORY
D=M
@VAR1
M=D

// GOTO LABEL
@LABEL
0; JMP



// IF VAR1<VAR2 GOTO LABEL
@VAR1
D=M
@VAR2
D=D-M
@LABEL
D; JLT


// IF VAR1<=VAR2 GOTO LABEL
@VAR1
D=M
@VAR2
D=D-M
@LABEL
D; JLE


// IF VAR1==VAR2 GOTO LABEL
@VAR1
D=M
@VAR2
D=D-M
@LABEL
D; JEQ


// IF VAR1>=VAR2 GOTO LABEL
@VAR1
D=M
@VAR2
D=D-M
@LABEL
D; JGE

// IF VAR1>VAR2 GOTO LABEL
@VAR1
D=M
@VAR2
D=D-M
@LABEL
D; JGT



// RETURN
@SI					// LOAD ADDRESS OF ORIGIN IN A
D=M+1				// D IS THE NEXT POSITION
0; JMP

// GOSUB LABEL
@#LINE				//#LINE IS A KEY TO THE MACRO-PROCESSOR TO CHANGE IT 
D=A					//BY THE LINE NUMBER OF INSTRUCTION
@SI
M=D

@LABEL
0; JMP				// This is similar to a GO TO, but it defines 
