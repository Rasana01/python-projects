QUESTION = input("What is the answer to the question of life, universe and everything? ").lower().strip()

match QUESTION:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")