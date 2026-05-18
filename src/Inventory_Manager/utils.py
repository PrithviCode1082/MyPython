def kv(item_stats):
    keys = list(item_stats.keys())
    val = list(item_stats.values())
    return f"{keys[0]} : {val[0]} | {keys[1]} : {val[1]} | {keys[2]} : {val[2]}"

def printInventory(inv):
    i = 1
    for section in inv.keys():
        print(f"{i}) {section}: ")
        for item in inv[section].keys():
            print(f" * {item} - {kv(inv[section][item])}")
        i += 1
        print()
