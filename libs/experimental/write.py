import os, json

with open("data.json", "rb") as f:
    data = json.load(f)


with open("items.txt", "a") as f:
    for key, value in data.items():
        item_name = data[key]['name']
        item_price = data[key]['price']
        disp = f"{item_name} = ${item_price}"
        print(disp)
        f.write(f"{disp}\n")
