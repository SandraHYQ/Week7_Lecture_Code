# Import csv module
import csv

#Define variables
regions = []
regions_revenue = {}
regions_units = {}

current_regions = ""
current_revenue = 0.0
current_units = 0

total_units = 0
total_rev = 0.0

# Import input file
with open("500000 Sales Records.csv", "rt") as Sales_Records:

    # Read input file
    reader = csv.reader(Sales_Records, delimiter=",")

    # Start without header.
    row = next(reader)

    # Looping input file
    for row in reader:

        # Get the current row values
        current_regions = row[0]
        current_units = row[8]
        current_revenue = row[11]

        if not current_regions in regions_units:
            regions_units[current_regions] = int(current_units)
        else:
            regions_units[current_regions] = \
                (regions_units[current_regions]) \
                + int(current_units)

        if not current_regions in regions_revenue:
            regions_revenue[current_regions] = float(current_revenue)
        else:
            regions_revenue[current_regions] = \
                regions_revenue[current_regions] + float(current_revenue)

    regions = list(regions_units.keys())

#Display the report head
print("Sales Report\n------------\nProduced on: 2020-02-10\n")

# Displayed all regions in Sales_Records
print("Regions analysed: ", end="")
for r in regions:
    print(r, end=", ")
print()

#Display Totals per region
print("\nTOTALS PER REGION\n")

for r in regions:
    print(r)
    print("Total units sold        : ", "{0}".format(regions_units[r]))
    print("Total revenue           : ", "${0:.2f}".format(regions_revenue[r]))

    average = regions_revenue[r] / regions_units[r]
    print("Average revenue per unit: ", "${0:.2f}".format(average))
    print()

    total_units += regions_units[r]
    total_rev += regions_revenue[r]

print("Grand Total units sold  : ", "{0}".format(total_units))
print("Grand Total revenue     : ", "${0:.2f}".format(total_rev))

average = total_rev / total_units
print("Average revenue per unit: ", "${0:.2f}".format(average))
print()
