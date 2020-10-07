import Data


print(f"Here are the available starters{Data.Starters_string[0]}")

while True:
    Is_Starter = input("What starter would you like to view? (gens 1-3): ")
    for i in Data.starters:
     if Is_Starter in i:
        Starter_index = i.index(Is_Starter)
        print()
    break
    print("Not a Starter from available starters.")

