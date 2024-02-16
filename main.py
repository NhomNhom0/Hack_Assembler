from WhiteSpace import WhiteSpaceHandler

while True:
    path = input("Please enter path: ")
    result = WhiteSpaceHandler(path)
    if not isinstance(result, str):
        print(result)
        break  # Exit the loop if WhiteSpaceHandler returns a list of strings
    else:
        print(result)