color_input = input("Enter comma-separated color names: ")
color_list = [color.strip() for color in color_input.split(',')]

if color_list:
    print("First color:", color_list[0])
    print("Last color:", color_list[-1])
else:
    print("No colors entered.")
