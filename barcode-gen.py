from barcode import EAN13
from barcode.writer import ImageWriter
from random import randint
import os, datetime, json, shutil

'''
    This script generates barcodes and saves them as svg files.
    This script does not need to be packaged with the application.
'''
# Each item will have a name, price, category, and barcode
class Item:
    def __init__(self, name, price, category, barcode, barcode_path, image_path):
        self.name = name
        self.price = price
        self.category = category
        self.barcode = barcode
        self.barcode_path = barcode_path
        self.image_path = image_path

# Generate barcodes and save them as svg files
def barcode_gen(num_barcodes):
    # Initialize the barcode lists
    barcode_path = []
    barcode_value = []

    # Set the temporary output directory
    now = datetime.datetime.now()
    output_dir = now.strftime("%Y-%m-%d-%H-%M-%S")
    os.makedirs(output_dir, exist_ok=True)

    # Generate num barcodes and save them as svg files, starting from 1
    for i in num_barcodes:
        fullname = str(randint(100000000000, 999999999999))
        barcode_location = f"{output_dir}/{fullname}.png"
        with open(barcode_location, "wb") as f:
            EAN13(fullname, writer=ImageWriter()).write(f)
        barcode_path.append(barcode_location)
        barcode_value.append(fullname)
        

    return barcode_path, barcode_value, output_dir


def main():
    
    # Ask user how many barcodes they want to generate
    total_barcodes = os.listdir('pngs/Foods')

    # Generate total_barcodes barcodes and save them as svg files, starting from 1
    barcode_path, barcode_value, temp = barcode_gen(total_barcodes)

    # Initialize the item list
    complete_inventory = {}

    # Ask user for item information
    for i, value in enumerate(barcode_value):

        # Get the item information from user
        name = (total_barcodes[i].split('.'))[0]
        price = input(f"What is the price of item {name}? ")
        category = input(f"What is the category of item {name}? ")
        barcode = value
        item = Item(name,
                    price,
                    category,
                    barcode,
                    barcode_path=f"assets/{name}/{barcode}.png",
                    image_path=f"assets/{name}.png"
                    )


        # Add the item to the complete inventory
        complete_inventory[item.name] = {
            "barcode": item.barcode,
            "barcode_path": item.barcode_path,
            "category": item.category,
            "image_path": item.image_path,
            "price": item.price,
        }

        # Move the barcode to the assets folder
        os.makedirs(f"assets/{item.name}", exist_ok=True)
        shutil.move(barcode_path[i], f"assets/{item.name}")
        shutil.move(f"pngs/Foods/{item.name}.png", f"assets/{item.name}")

    # Save the data
    with open("data.json", "w") as f:
        json.dump(complete_inventory, f, indent=4)
    
    # Delete the temporary directory
    os.rmdir(temp)
    

if __name__ == '__main__':
    main()
