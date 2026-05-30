import pandas as pd

# create a dataframe (like a table)
data = {
    "Name" : ["Messi", "Ronaldo", "Mbappe", "Neymar", "Salah"],
    "Age" : [36, 39, 25, 32, 31],
    "Goals" : [50, 45, 40, 30, 35],
    "Country": ["Argentina", "Portugal", "France", "Brazil", "Egypt"]
     
}
df = pd.DataFrame(data)
print(df.info())
print(df.describe())
print(df.sort_values("Goals", ascending=False))
print(df[df["Age"] < 32])
df.to_csv("players.csv", index=False)
print("Saved to players.csv")

df2 = pd.read_csv("players.csv")
print(df2)