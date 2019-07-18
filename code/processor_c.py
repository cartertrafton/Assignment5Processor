from enum import Enum

#ALU OPERATIONS
class ALU_opcode(Enum):
    ADD = 1
    SUB = 2

class InstructionReg:
    opcode=0
    Format=''
    Rd=0
    Rn=0
    Rm=0
    Imm=0
    addr=0
    def __init__(self, instruc):
        instruc=instruc.replace(",","")     ##format instruction 
        instruc=instruc.replace("#","")     ##for code to read
        instruc=instruc.replace("XZR","0")  ##
        instruc=instruc.replace("X","")     ##
        instruc=instruc.replace("[","")     ##
        instruc=instruc.replace("]","")     ##
        instruc=instruc.split()             #seperate instruction into addressable entities
        self.opcode=instruc[0]
        if(self.opcode=='ADD' or self.opcode=='SUB' or self.opcode=='AND' or self.opcode=='ORR'):
            self.Format='R'
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])
            self.Rm=int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Rm)
        elif (self.opcode=='LDUR' or self.opcode=='STUR'):
            self.Format='D'
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])
            self.addr= int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.addr)
        elif(self.opcode=='ADDI' or self.opcode=='SUBI'):
            self.Format='I'
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])
            self.Imm=int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Imm)
        elif(self.opcode=='B' or self.opcode=='CBZ'):
            self.Format='B'
            self.addr=int(instruc[1])
            if(self.opcode=='CBZ'):
                self.Rd=int(instruc[1])
                self.addr=int(instruc[2])
            print(self.opcode, self.Rd, self.addr)
class ALU():
    def __init__(self):
        self.input_A = 0
        self.input_B = 0
        self.output = 0

    # This will execute whatever operation called at the method
    def execute_instruction(self,in_a,in_b,op_code):
        self.input_A = in_a
        self.input_B = in_b

        if( op_code == ALU_opcode.ADD):
            # ADD TWO INPUTS and output  the sum
            self.addition()
        if (op_code == ALU_opcode.SUB):
            # Subtract TWO INPUTS and output the difference
            self.subtract()

    # Add operation
    def addition(self):
        self.output = self.input_A + self.input_B

    # Subtract operation
    def subtract(self):
        self.output = self.input_A - self.input_B



class proccessor():
    def __init__(self):
        self.PC = 0
        self.General_ALU = ALU()






def decode_instruction():
    pass
