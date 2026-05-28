score = 0
Q1 = input("who is the football best player of all the time? ").upper().strip()

if Q1 == "MESSI":
    print("Correct✅")
    score = score + 1
else:
    print("Wrong❌")
    
Q2 = input("which country won 2022 world cup? ").upper().strip()
if Q2 == "ARGENTINA":
    print("correct✅")
    score = score + 1
else:
    print("wrong❌")     

print(f"you scored {score}/2!")       
        