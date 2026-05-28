coke = 50

while coke > 0:
    print(f"amount due:{coke}")
    coin = int(input("insert a coin: "))
    if coin in [25,10,5]:
        coke -= coin
        
print(f"change owed: {max(0, -coke)}")        