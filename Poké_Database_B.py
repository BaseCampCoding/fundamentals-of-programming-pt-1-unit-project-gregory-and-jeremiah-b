import Data


print(f"Here are the available starters{Data.Starters_string[0]}")

while True:
   Is_Starter = input("What starter would you like to view? (gens 1-3): ")
   for i in Data.starters:
      if Is_Starter in i:
         Starter_index = i.index(Is_Starter)
         print()
         break
      else:
         print("Not a Starter from available starters.")


while True:
   print(f"Here are the types{Data.types[0]}")
   Type_categories = input("Pick a type for a list of Pokemon in that type. (gens 1-3) (q to quit) :")
   for i in Data.starters[int(0)]:
      if Type_categories in Data.types:
         Type_index = Data.types.index(Type_categories)
         break
      else:
         print("Not a valid type. Please choose valid types")