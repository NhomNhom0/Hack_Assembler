# This function will read .asm file and remove all unnecessary characters 
# (eg: empty lines/indentation, line comments, In-line comments)

def WhiteSpaceHandler(path):
    try:
        strings = []
        #Opening the file in read mode
        with open(path, 'r') as file:
            # Reading the contents of the file line by line
            for line in file:
                # Removing comments starting with //
                line = line.split("//")[0].strip()
                # Remove all whitespace characters
                line = line.replace(" ", "")
                # Extracting strings from the line
                line_strings = line.split()
                # Adding non-empty strings to the list
                for i in line_strings:
                    if i:
                        strings.append(i)
        return strings
    except FileNotFoundError:
        return "File not found. Please make sure the path is correct."
    except Exception as e:
        return f"An error occurred: {e}"
        
     
