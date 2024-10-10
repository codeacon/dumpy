import sys

def resolve_value(v):
    if v in OPERATIONS:
        return OPERATIONS[v]
    if v in SYMBOL_TABLE:
        return SYMBOL_TABLE[v]
    return v 

def assign(symbol, val):
    print("assign called")
    SYMBOL_TABLE[symbol] = resolve_value(val)

def add(target, val):
    SYMBOL_TABLE[target] += resolve_value(val)

def printout(v):
    print("print called")
    print(resolve_value(v))

OPERATIONS = {
    "=": assign,
    "+": add,
    "`": printout,
}
OP_KEYS = OPERATIONS.keys()
SYMBOL_TABLE = {}

NUMBER_TABLE = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "_"]

class NumberBuilder:
    def __init__(self):
        self.numbers = []
    def addChar(self, num: str):
        self.numbers += num
    def parse(self):
        return int(''.join(self.numbers))

class SymbolBuilder:
    def __init__(self):
        self.chars = []
    def addChar(self, char: str):
        self.chars += char
    def parse(self):
        return ''.join(self.chars)

class Statement:
    def __init__(self):
        self.operation = None
        self.operands = []

    def execute(self):
        if self.operation:
            operands = [op.parse() for op in self.operands]
            print(operands)
            self.operation(*operands)
    
def parse(line):
    if not line:
        return
    len_line = len(line)
    idx = 0
    cur_statement = Statement()
    cur_builder = None
    for char in line:
        if char in OP_KEYS:
            print(f"{char} op")
            if cur_builder:
                cur_statement.operands.append(cur_builder)
            cur_builder = None
            cur_statement.operation = OPERATIONS[char]
        elif char == " ":
            print(f"{char} space")
            if cur_builder:
                cur_statement.operands.append(cur_builder)
            cur_builder = None
        else:
            if char == "\n":
                print(f"newline")
                cur_statement.operands.append(cur_builder)
            elif cur_builder:
                print(f"{char} to builder")
                cur_builder.addChar(char)
            elif char in NUMBER_TABLE:
                print(f"{char} num:")
                cur_builder = NumberBuilder()
                cur_builder.addChar(char)
            else:
                print(f"{char} symbol:")
                cur_builder = SymbolBuilder()
                cur_builder.addChar(char)

    print(line)
    cur_statement.execute()
    input()

with open(sys.argv[1]) as fh:
    for line in fh:
        parse(line)
