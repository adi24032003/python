input_str = input("Enter text:\n")
first_char = input_str[0]
result = first_char + input_str[1:].replace(first_char, "$")
print(result) 
