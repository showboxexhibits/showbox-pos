from barcode import EAN13
from barcode.writer import SVGWriter
from random import randint
import os
import datetime

'''
    This script generates barcodes and saves them as png files.
    This script does not need to be packaged with the application.
'''

def main():

    # Set the output directory
    now = datetime.datetime.now()
    new_dir = now.strftime("%Y-%m-%d-%H-%M-%S")
    output_dir = f'completed-barcodes/{new_dir}'
    os.makedirs(output_dir, exist_ok=True)

    # Ask user how many barcodes they want to generate
    total_barcodes = input("How many barcodes do you want to generate? ")

    # Generate total_barcodes barcodes and save them as svg files, starting from 1
    for i in range(1, int(total_barcodes) + 1):
        fullname = f"barcode_{i}"
        with open(f"{output_dir}/{fullname}.svg", "wb") as f:
            EAN13(str(randint(100000000000, 999999999999)), writer=SVGWriter()).write(f)

if __name__ == '__main__':
    main()
