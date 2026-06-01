import random

team = {
    "name": "Rayon ",
    "budget": 1000000,
    "players": ["Messi", "Ronaldo", "Mbappe" ], 
    "points": 0,
    "wins":0,
    "losses": 0,
    "draws":0,
}

def show_team():
    print(f"\n{'='*30}")
    print(f"  {team['name']}")
    print(f"{'='*30}")
    print(f"Budget: ${team['budget']:,}")
    print(f"Points: {team['points']}")
    print(f"W:{team['wins']} D:{team['draws']} L:{team['losses']} ")
    print(f"Players: {', '.join(team['players'])}")
    print(f"{'='*30}")
    
def main():
    print("🏆 Welcome to Fotball Manager!")
    print(f"You are managing {team['name']}")
    
    while True:
        print("\nWhat do you want to do? ")
        print("1. View team.") 
        print("2. Play match")
        print("3. Buy player")
        print("4. Sell player")
        print("5. Quit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            show_team()
        elif choice == "2":
            play_match()
        elif choice == "3":
            buy_player()
        elif choice == "4":
            sell_player()
        elif choice == "5":
            print("Thanks for playing!👏")                
            break
        else:
            print("Invalid choice!")

def play_match():
    opponents = ["APR FC", "Police Fc", "Musanze Fc", "AS Kigali", "Gorilla Fc"]
    opponent = random.choice(opponents)
    
    our_goals = random.randint(0, 4)
    their_goals = random.randint(0, 4)
    
    print(f"\n⚽ {team['name']} vs {opponent}")   
    print(f"Final Score: {our_goals} - {their_goals}")  
    
    if our_goals > their_goals:
        print("🥳 You won!")
        team["wins"] += 1 
        team["points"] += 3
        team["budget"] +=  50000
        print("You earned $50,000!")
    elif our_goals == their_goals:
        print("🤝 It's a DRAW!")
        team["draws"] += 1
        team["points"] += 1
        team["budget"] += 10000
        print("You earned $10,000!")
    else:
        print("😢 You LOST!")
        team["losses"] += 1
        team["budget"] -= 20000
        print("You lost $20,000!")    
     
def buy_player():
    available = ["salah", "neymar", "benzema", "lewandowski", "halland", ] 
    print("\n🛒 Available player: ")
    for i, player in enumerate(available, 1):
        print(f"{i}. {player} - $100,000 ")
        
    name = input("Enter the player name to buy: ").strip()
        
        
    if name in available:
        if team["budget"] >=100000:
            team["players"].append(name) 
            team["budget"] -= 100000
            print(f"✅ {name} signed for $100,000!")
        else:
            print(f"❌ Not enough budget!")
    else:
        print("❌ Player not found!")
        
def sell_player():
    if len(team["players"]) <= 1:
        print("❌ You need at least 1 player!")
        return                                   
    
    show_team()
    name = input("Enter player name to sell: ").strip()
    
    if name in team["players"]:   
        team["players"].remove(name)
        team["budget"] += 80000
        print(f"✅{name} sold for 80,000!")
    else:
        print("❌ Player not found!")       
main()            
            