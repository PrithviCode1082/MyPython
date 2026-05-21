from database import inventory_data as inv

def kv(item_stats):
    keys = list(item_stats.keys())
    val = list(item_stats.values())
    return f"{keys[0]} : {val[0]} | {keys[1]} : {val[1]} | {keys[2]} : {val[2]}"

def print_inventory_keys():
    i = 0
    for sec in inv.keys():
        print(f"{i+1}) {sec}")
        i += 1
    num = int(input("Enter the section you wanna configure: "))
    section = list(inv.keys())[num-1]
    i = 0
    print(f"{section}:")
    for item, stats in inv[section].items():
        print(f"{i+1}) {item} - {kv(stats)}")
        i+=1

def print_inventory():
    i = 1
    for section in inv.keys():
        print(f"{i}) {section}: ")
        for item in inv[section].keys():
            print(f" * {item} - {kv(inv[section][item])}")
        i += 1
        print()
