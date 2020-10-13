import Data


while True:
    Awnser=input("What do you want to search by? names,types,weaknesses,generations\n")
    if Awnser == "names":
        while True:
            print(f"Here are the available starters{Data.Starters_string[0]}")
            Is_Starter = input("What starter would you like to view? (gens 1-3) (q to quit): ").lower()
            if Is_Starter == "q":
                    break
            for i in Data.Starters:
                if i[0] == Is_Starter:
                    count = 0
                    while count < len(i):
                        print(Data.information[count], i[count])
                        count += 1
                    print("")
                    break
                elif i[0] != Is_Starter and i == Data.Starters[-1]:
                    print("Not a Starter from available starters! Please choose a valid starter.")
    
    
    elif Answer == "types":
        while True:
            check_if_found_valid = False
            Type_categories = input("Use a valid type to get a list of pokemon in requested type. (gens 1-3) (press 'q' to quit): ").lower
            if Type_categories == "q":
                    break
            for i in Data.Starters:
                if i[2] == Type_categories:
                    print(i[0])
                    check_if_found_valid = True
                elif i[2] != Type_categories and i == Data.Starters[-1] and check_if_found_valid == False:
                    print("Not a valid type. Please choose valid types")
    
    
    elif Answer == "weaknesses":
        while True:
            Weaknesses = input("What type do you want to see the advantage of? weak to water, weak to grass, weak to fire (q to quit): \n").lower()
            if Weaknesses == "q":
                    break
            for i in Data.Starters:
                if i[4] == Weaknesses:
                    print(i[0] + " is " + Weaknesses)
                elif i[4] != Weaknesses and i == Data.Starters[-1]:
                    print ("Not a valid weakness. Please choose a valid weakness")
   
   
    elif Answer == "generations":
        while True:
            check_if_found_valid = False
            generations = input("Pick a generation for a list of pokemon. (gens 1-3) (press 'q' to quit): ").lower()
            if generations == "q":
                    break
            for i in Data.Starters:
                if i[3] == generations:
                    print(i[0])
                    check_if_found_valid = True
                elif i[2] != generations and i == Data.Starters[-1] and check_if_found_valid == False:
                    print("Not a proper 'gens'. Please choose valid 'gens'")
    elif Awnser == "Exit":
        break