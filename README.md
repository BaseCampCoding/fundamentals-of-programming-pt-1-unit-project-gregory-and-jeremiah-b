# Unit project 1
## Gregory and Jeremiah
## Goals
Our goal was to create a new search feature that is more specific than the one in the Pokémon games. We have made it where you can search for the names of starters, their types, what they are weak to and there generation they were added.
## Poké_Database_B.py
This is the main file where all of our work is put in and ran. It has all of our loops and all of the needed print statements. 
## Data.py
This is the file holding all of our Data and is what our lists search through for everything.
## Usages
```
Awnser=input("What do you want to search by? Names, types, weaknesses,generations\n") # has the user pick a search option 

# If "name" is chosen it asks for 
Is_Starter = input("What starter would you like to view? (gens 1-3) (q to quit):").lower() 
# This allows them to see the information of a specific pokémon.

# If "types" is chosen it asks 
Type_categories = input("Use a valid type to get a list of pokémon in requested type. (gens 1-3) (press 'q' to quit): ")
# This allows the user to say a specific type and it shows all pokémon of the specified type.

#If "weaknesses is chosen it asks
Weaknesses = input(f"What type do you want to see the advantage of? {Weaknesses_types} (q to quit): \n").lower()
# this shows Pokémon that are weak to what the user inputs.

#It "generations" is chosen it asks 
generations = input("Pick a generation for a list of pokemon. (gens 1-3) (press 'q' to quit): ")
# this shows the pokemon from whatever generation the user requests.
```
## Contributions
We are very welcome and accepting of contributions but please open an issue and we can discuss them.

