from WhiteSpace import WhiteSpaceHandler
from SymbolTable import SymbolsHandler

while True:
    path = input("Please enter path: ")
    instruction = WhiteSpaceHandler(path)
    if not isinstance(instruction, str):
        break  # Exit the loop if WhiteSpaceHandler returns a list of strings

symbol_table = SymbolsHandler(instruction)
print(symbol_table)
