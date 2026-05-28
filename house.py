name = input("what's your name? ")

match name:
    case "Harry" | "hermione" | "ron":
        print("Gryffindor")
    case "Dranco":
        print("Slytherin")
    case _:
        print("who?")        
        