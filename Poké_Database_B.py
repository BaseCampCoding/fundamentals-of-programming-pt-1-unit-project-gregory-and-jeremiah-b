import Data


print(f"Here are the available starters{Starters[0]}")
def Is_A_Starter(Is_Starter):
    while True:
        Is_Starter = input("What starter would you like to view? (gens 1-3) (q to quit) : ").lower()
        if Is_Starter in (starters):
            return Is_Starter 

