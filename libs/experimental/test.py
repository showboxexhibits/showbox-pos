import json, sys

def menu_disp():
    print("Select one of the following options:")
    print("1. Image of item")
    print("2. Price of item")
    print("3. Category of item")
    print("4. Scan new item")
    print("5. Close application")
    ans = input()
    return ans

def scan_item_prompt():
    ans = input("Scan item:\n")
    return ans

with open("data.json", "rb") as f:
    data = json.load(f)

ans = scan_item_prompt()

while True:
    if ans in data.keys():
        print(f"\n\n{data['ans']} selected.")
        ans = menu_disp()
        if int(ans) == 1:
            pass
        if int(ans) == 2:
        if int(ans) == 3:
        if int(ans) == 4:
        if int(ans) == 5:
            sys.exit()
    else:
        print("Error: Item not found in database.\nTry again.")
        scan_item_prompt()
