import os
from elements.WhiteSpace import WhiteSpaceHandler
from elements.SymbolTable import SymbolsHandler
from elements.Instructions import parse_line

instructions = []

while True:
    path = input("Please enter path: ")
    list = WhiteSpaceHandler(path)
    if not isinstance(list, str):
        break  # Exit the loop if WhiteSpaceHandler returns a list of strings
    else:
        print(list)

symbol_table = SymbolsHandler(list)


for line in list:
    instruction = parse_line(line, symbol_table)
    if instruction is not None:
        instructions.append(instruction)


# Define the path
new_path = path.replace("asm", "hack").replace(".asm", ".hack")

# Create the directory if it doesn't exist
directory = os.path.dirname(new_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Write data to the new file
with open(new_path, 'w') as file:
    for item in instructions:
        file.write(str(item) + '\n')

print(f"Convert success...\nHack file saved at {new_path}")
