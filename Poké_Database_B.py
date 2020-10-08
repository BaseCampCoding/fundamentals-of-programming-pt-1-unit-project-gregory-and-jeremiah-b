import Data


print(f"Here are the available starters{Data.Starters_string[0]}")

while True:
    Is_Starter = input("What starter would you like to view? (gens 1-3): ")
    for i in Data.Starters:
     if i[0]== Is_Starter:
         print(i)
         break
     elif Is_Starter == "q":
         quit()
     elif i[0]!= Is_Starter:
         print("Not a Starter from available starters! Please choose a valid starter.")


while True:
    Type_categories = input("Use a valid type to get a list of pokemon in requested type. (gens 1-3): ")
    for i in Data.Starters:
     if i[2]== Type_categories:
        print(i)
        break
     elif Type_categories == "q":
         quit() 
     elif i[2]== Type_categories:
        print("Not a valid type. Please choose valid types")
