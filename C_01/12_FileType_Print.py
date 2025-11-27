filename = input("Enter the file name: ")
if '.' in filename:
    extension = filename.split('.')[-1]
    print("File extension: ", extension)
else:
    print("No extension found in the file name.")
