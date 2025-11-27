s = "python"
if len(s) < 2:
    result = s
else:
    result = s[-1] + s[1:-1] + s[0]
print(result)
