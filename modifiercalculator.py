modifier_names = ["atk", "dura", "crit", "throw", "spread", "zoom", "rapid", "surf", "guard"]

def get_mods(rupees):
    modifiers = []
    
    for i, mod in enumerate(modifier_names):
        if rupees & (0b00000001 << i):
            modifiers.append(mod)
    return modifiers
    
def list_mod():
    rupees = int(input())
    modifiers = get_mods(rupees)           
    print(", ".join(modifiers))

def find_mod():
    whitelist = input("Whitelist: ").split(" ")
    blacklist = input("Blacklist: ").split(" ")
    successes = []
    for i in range(0, 2500, 10):
        mods = get_mods(i)
        if set(whitelist).issubset(mods) and set(blacklist).isdisjoint(mods):
            successes.append(str(i))
    if len(successes) == 0:
        print("Failed to find a valid sell value")
    else:
        print(", ".join(successes))

def main():
    while True:
        op = input("Input an operation or h to get help: ")
        if op == "f":
            find_mod()
        elif op == "l":
            list_mod()
        elif op == "q":
            break
        elif op == "h":
            print('''Valid commands:
1) l - Lists the modifiers for a given sell value
2) f - Finds all sell values below 2500 which correspond to the given space-separated whitelist and blacklist
3) q - Exits the program
Modifier list:
1) atk - Affects attack damage
2) dura - Affects durability (doesn't increase actually value)
3) crit - Allows a weapon to crit
4) throw - Long throw on weapons
5) spread - Gives bows multishot
6) zoom - Allows bows to zoom in when aimed
7) rapid - Affects bow draw speed (requires extremely high values, not recommended)
8) surf - Increases surfing speed
9) guard - Affects shield guard''')
        else:
            print("Invalid operation")

if __name__ == "__main__":
    main()
