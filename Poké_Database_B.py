import Data
Awnser=input("What do you want to search by? starters,types,weaknesses,generations")
if Awnser == "starters":
    while True:
        Is_Starter = input("What starter would you like to view? (gens 1-3) (q to quit):").lower()
        for i in Data.Starters:
            if i[0] == Is_Starter:
                print(i)
                break
            elif Is_Starter == "q":
                quit()
            elif i[0] != Is_Starter and i == Data.Starters[-1]:
                print("Not a Starter from available starters! Please choose a valid starter.")
elif Awnser == "types":
    while True:
        check_if_found_valid = False
        Type_categories = input("Use a valid type to get a list of pokemon in requested type. (gens 1-3) (press 'q' when done searching): ")
        for i in Data.Starters:
            if i[2] == Type_categories:
                print(i[0])
                check_if_found_valid = True
            elif Type_categories == "q":
                quit() 
            elif i[2] != Type_categories and i == Data.Starters[-1] and check_if_found_valid == False:
                print("Not a valid type. Please choose valid types")
elif Awnser == "weaknesses":
    Weaknesses_types=['weak to water, weak to grass, weak to fire']
    while True:
        Weaknesses = input(f"What type do you want to see the advantage of? {Weaknesses_types} (q to quit): \n").lower()
        for i in Data.Starters:
            if i[3] == Weaknesses:
                print(i[0] + " is " + Weaknesses)
elif Awnser == "generations":