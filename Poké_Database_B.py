#Bulbasaur, Charmander, Squirtle, Pikachu, Chikorita
#Cyndaquil, Totodile, Treecko, Torchic, Mudkip
print("Here are the available starters\n(articuno)")
Articuno = [
    144,
    ("Ice", "flying"),
    "Doesn't evolve",
    "Articuno is a legendary bird Pokémon that can control ice."
    "The flapping of its wings chills the air. As a result, it is said that when this Pokémon flies, snow will fall."
]
while True:
    response = input("What starter would you like to view? (gens 1-3) (q to quit) : ").lower()
    if response == 'articuno':
        print(Articuno[:5])
        break
    elif response == 'q':
        break
Cyndaquil=[
    144,
    ("Fire"),
    "evolves into Quilava",
    "It is timid, and always curls itself up in a ball."
    "If attacked, it flares up its back for protection"
    ]
