
def SymbolsHandler(list):
    # Predefined symbols
    SYMBOLS = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }

    # Add R0 to R15 to symbols
    for i in range(16):
        SYMBOLS[f'R{i}'] = i
    
    next_address = 16
    address = 1
    for line in list:
        if line.startswith('('):
            symbol = line[1:-1]
            SYMBOLS[symbol] = address
        elif line.startswith('@'):
            variable = line[1:]
            if not variable.isdigit() and variable not in SYMBOLS:
                SYMBOLS[variable] = next_address
                next_address += 1
            address += 1
        else:
            address += 1
    
    return SYMBOLS
