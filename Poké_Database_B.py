Starters= [" \nbulbasaur, charmander, squirtle, pikachu, \nchikorita, cyndaquil, totodile,\ntreecko, torchic, mudkip"]
print(f"Here are the available starters{Starters[0]}")
while True:
    response = input("What starter would you like to view? (gens 1-3) (q to quit) : ").lower()
    if response == 'articuno':
        print(cyndaquil[:5])
        break
    elif response == 'q':
        break
Bulbasaur=[]
cyndaquil=[
    155,
    ("Fire"),
    "evolves into Quilava",
    "It is timid, and always curls itself up in a ball."
    "If attacked, it flares up its back for protection"
    ]
totodile=[
    158,
    ("water"),
    "Its well-developed jaws are powerful and capable of crushing anything."
    "Even its trainer must be careful."
]
treecko=[
    252,
    ("grass"),
    "Evolves into Grovyle"
    "Treeko has small hooks on the bottom of its feet that enable it to scale vertical walls."
    "This POKéMON attacks by slamming foes with its thick tail."
]
torchic=[
  255,
  ("fire"),
  "evolves into Combusken",
  "torchic sticks with its trainer, following behind with unsteady steps."
  "This pokémon breathes fire of over 1,800 degrees F, including fireballs that leave the foe scorched black."
]

types = [
    "fire"
    "water"
    "grass"
    "electric"
    "poison"
]

fire = [
    "charmander"
    "cyndaquil"
    "torchic"
]

water = [
    "squirtle"
    "totodile"
    "mudkip"
]

grass = [
    "bulbasaur"
    "chikorita"
    "treecko"
]

electric = ["pikachu"]

poison = ["bulbasaur"]