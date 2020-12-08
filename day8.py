from utils import FileUtils

class HandHeldConsole:
    def __init__(self, instructions):
        self.original_instructions = instructions
        self.clear_memory()
    
    def clear_memory(self):
        self.accumulator, self.index, self.memory = 0, 0, []
        self.instructions = list(self.original_instructions)

    def get_operation_func(self, op):
        return {
            'acc': self.acc,
            'jmp': self.jmp,
        }.get(op, lambda arg: None)

    def acc(self, arg):
        self.accumulator += int(arg)

    def jmp(self, arg):
        return int(arg)

    def run(self):
        while True:
            if self.index in self.memory:
                return -1
            elif self.index == len(self.instructions):
                return 0
            self.memory.append(self.index)
            op, arg = self.instructions[self.index].split(" ")
            self.index += self.get_operation_func(op)(arg) or 1

    def fix_code(self, op1='jmp', op2='nop'):
        op_index = 0
        while self.run() != 0:
            self.clear_memory()
            swap_index, op = [(i, op) for i, op in enumerate(self.instructions) if op1 in op or op2 in op][op_index]
            self.instructions[swap_index] = self.instructions[swap_index].replace(op.split(" ")[0], op1 if op2 in op else op2)
            op_index += 1

if __name__ == "__main__":
    hhc = HandHeldConsole(FileUtils.input())
    hhc.run()
    print(hhc.accumulator) 
    hhc.fix_code()
    print(hhc.accumulator) 