import Data


print(f"Here are the available starters{Data.Starter[0]}")

while True:
    Is_Starter = input("What starter would you like to view? (gens 1-3): ")
    for i in Data.starters:
     if i[0]== Is_Starter:
        print(i)
    break
    print("Not a Starter from available starters!")


while True:
    Type_categories = input("Use a valid type to get a list of pokemon in requested type. (gens 1-3): ")
    for i in Data.starters:
     if i[2]== Is_Starter:
        print(i)
    break
    print("Not a valid type. Please choose valid types")