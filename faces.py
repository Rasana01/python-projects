def convert(f):
    f = f.replace(":)", "😊")
    f = f.replace(":(", "😔")
    return f

def main():
    text = input("input:")
    print(convert(text))
    
main()    