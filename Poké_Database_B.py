import Data


print(f"Here are the available starters{Data.Starters[0]}")

while True:
    Is_Starter = input("What starter would you like to view? (gens 1-3): ")
    for i in Data.Starters:
     if i[0]== Is_Starter:
        print(i)
    break
    print("Not a Starter from available starters!")