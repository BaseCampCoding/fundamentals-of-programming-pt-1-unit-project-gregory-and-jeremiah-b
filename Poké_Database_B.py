#Bulbasaur, Charmander, Squirtle, Pikachu, Chikorita
#Cyndaquil, Totodile, Treecko, Torchic, Mudkip
print("Here are the available starters\n(articuno)")
while True:
    response = input("What starter would you like to view? (gens 1-3) (q to quit) : ").lower()
    if response == 'articuno':
        print(Articuno[:5])
        break
    elif response == 'q':
        break
Cyndaquil=[
    155,
    ("Fire"),
    "evolves into Quilava",
    "It is timid, and always curls itself up in a ball."
    "If attacked, it flares up its back for protection"
    ]
