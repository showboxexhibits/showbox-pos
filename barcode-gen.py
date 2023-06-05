from barcode import EAN13
from barcode.writer import SVGWriter

'''
    This script generates barcodes and saves them as png files.
    This script does not need to be packaged with the application.
'''

def main():

    # Set the output directory
    output_dir = 'completed-barcodes'

    # Generate a barcode and save it as an svg file
    with open(f"{output_dir}/test.svg", "wb") as f:
        EAN13('111111111111', writer=SVGWriter()).write(f)

if __name__ == '__main__':
    main()
