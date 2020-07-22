"""CPU functionality."""

import sys

LDI = 0b10000010 
PRN = 0b01000111 # Print
HLT = 0b00000001  # Halt
MUL = 0b10100010  # Multiply
ADD = 0b10100000  # Addition
SUB = 0b10100001 # Subtraction
DIV = 0b10100011 # Division

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.registers = [0] * 8
        self.ram = [0] * 256
        self.pc = 0
        self.ir = 0
        

    def load(self):
        """Load a program into memory."""
        filename = sys.argv[1]

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        #    ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

        with open(filename) as f:
            for line in f:
                line = line.split("#")[0].strip()
                if line == "":
                    continue
                else:
                    self.ram[address] = int(line, 2)
                    address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == "DIV":
            self.reg[reg_a] /= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    def handleHLT(self):
        print("HLT")
        sys.exit(1)

    def handleLDI(self):
        register = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)

        self.reg_write(register, value)

        self.pc += 3
    
    def handlePRN(self):
        reg_num = self.ram_read(self.pc + 1)
        print(self.registers[reg_num])
    
    def ram_read(self, pc):
        return self.ram[self.pc]

    def ram_write(self, pc, value):
        self.ram[self.pc] = value

    def reg_read(self, pc):
        return self.reg[self.pc + 1]

    def reg_write(self, pc, value):
        self.reg[self.pc] = value


    def run(self):
        """Run the CPU."""
        self.pc = 0 
        running = True
        
        while running:
            self.ir = self.ram_read[self.pc]

            if self.ir == LDI:
                handleLDI()
            if self.ir == PRN:
                self.handlePRN()
            if self.ir == HLT:
                self.handleHLT()
            

