import sys

def resolve_value(v):
    if v in OPERATIONS:
        return OPERATIONS[v]
    if v in SYMBOL_TABLE:
        return SYMBOL_TABLE[v]
    if v.startswith('"') and v.endswith('"'):
        return v
    if "." in v:
        return float(v)
    return int(v)

def assign(symbol, value):
    SYMBOL_TABLE[symbol] = resolve_value(value)

def add(target, val):
    SYMBOL_TABLE[target] += resolve_value(val)

def subtract(target, val):
    target -= resolve_value(val)

def printout(v):
    print(resolve_value(v))

OPERATIONS = {
    ":": assign,
    "+": add,
    "-": subtract,
    "`": printout,
}
OP_KEYS = OPERATIONS.keys()
SYMBOL_TABLE = {}

def parse(line):
    if not line:
        return
    symbols = line.strip().split(" ")
    OPERATIONS[symbols[0]](*symbols[1:])

with open(sys.argv[1]) as fh:
    for line in fh:
        parse(line)
