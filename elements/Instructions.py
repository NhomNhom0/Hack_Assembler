
# A and C instruction prefix
A_intrstuction_prefix = "0"
C_intrstuction_prefix = "111"

# Jump codes
JUMP_CODES = {
    None : '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'
}

# Compute codes
COMP_CODES = {
    None: "0000000",
    "0" : "0101010",
    "1" : "0111111",
    "-1": "0111010",
    "D" : "0001100",
    "A" : "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1":"0011111",
    "A+1":"0110111",
    "1+A":"0110111",
    "D-1":"0001110",
    "A-1":"0110010",
    "D+A":"0000010",
    "A+D":"0000010",
    "D-A":"0010011",
    "A-D":"0000111",
    "D&A":"0000000",
    "A&D":"0000000",
    "D|A":"0010101",
    "A|D":"0010101",
    "M" : "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1":"1110111",
    "1+M":"1110111",
    "M-1":"1110010",
    "D+M":"1000010",
    "M+D":"1000010",
    "D-M":"1010011",
    "M-D":"1000111",
    "D&M":"1000000",
    "M&D":"1000000",
    "D|M":"1010101",
    "M|D":"1010101"
}

# handle A-instruction
def parse_a_instruction(line, symbol_table):
    address = line[1:]
    if address.isdigit():
        binary_address = bin(int(address))[2:]  # Convert address to binary, remove '0b' prefix
        padded_binary_address = binary_address.zfill(15)  # Pad binary address with zeros to make it 15 bits long
        return '0' + padded_binary_address  # Add '0' as the first bit
    else:
        if line.startswith("("):
            return None
        else:
            symbol_address = symbol_table[address]
            binary_address = bin(symbol_address)[2:]  # Convert address to binary, remove '0b' prefix
            padded_binary_address = binary_address.zfill(15)  # Pad binary address with zeros to make it 15 bits long
            return '0' + padded_binary_address  # Add '0' as the first bit

# handle C-instruction
def parse_c_instruction(line):
    if ";" in line:
        dest = "000"
        comp,jump = line.split(";")
    else:
        jump = None
        dest, comp = line.split("=")
    return '111' + COMP_CODES[comp] + dest_bin(dest) + JUMP_CODES[jump]

def dest_bin(dest):
    result = ['0'] * 3
    if 'A' in dest:
        result[0] = '1'
    if 'D' in dest:
        result[1] = '1'
    if 'M' in dest:
        result[2] = '1'
    return ''.join(result)

# handle all instruction and transform them into 16-bit binary
def parse_line(line, symbol_table,):
    if line.startswith("@") or line.startswith("("):
        return parse_a_instruction(line, symbol_table)
    else:
        return parse_c_instruction(line)
