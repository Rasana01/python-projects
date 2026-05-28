def start():
    print("you're a young footballer in Kigali.")
    print("A scout approaches you after training.")
    print("He offers you two options:")
    print("1. Trial at FC Barcelona")
    print("2. Trial at Real Madrid")
    choice = input("Which do you choose? madrid/barcelona)").lower().strip()
    if choice == "barcelona":
        barcelona()
    elif choice == "real madrid":
        madrid()
    else:
        print("invalid choice")
        
def barcelona():
    print("\nYou arrive at Camp Nou. Messi himself is watching!")
    choice = input("Do you shoot or pass? (shoot/pass): ").lower().strip()
    if choice == "shoot":
        print("\nGOAL! You score a screamer! Barcelona signs you! 🏆")
    elif choice == "pass":
        print("\nGood team play! But they want a striker. Try again next year. 😢")
    else:
        print("Invalid choice!")
        barcelona()
               
def madrid():
    print("\nYou arrive at Bernabeu. Ronaldo is in the stands!")
    choice = input("Do you dribble or shoot? (dribble/shoot): ").lower().strip()
    if choice == "dribble":
        print("\nYou beat 3 defenders! Real Madrid signs you! 🏆")
    elif choice == "shoot":
        print("\nThe shot hits the post. So close! Try again next year. 😢")
    else:
        print("Invalid choice!")
        madrid()

start()    