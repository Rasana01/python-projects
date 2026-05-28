name = input("camelcase: ")
result = ""
for char in name:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char
print(result)
            