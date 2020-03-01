import csv
import datetime
import locale
import sys
from money import Money

region_totals = {}
grant_total_units_sold = 0
grant_total_total_revenue = 0.0

# Used to format output
format_currency = "CAD"
format_locale = "en_CA"
locale.setlocale(locale.LC_ALL, format_locale)

try:
    with open("500000 Sales Records.csv", 'rt') as input_file:
        csv_reader = csv.reader(input_file)

        # Skip header row
        next(csv_reader)

        for current_row in csv_reader:
            region_name = current_row[0]
            region_units_sold = int(current_row[8])
            region_total_revenue = float(current_row[11])

            if region_name in region_totals.keys():
                region_totals[region_name]["Units Sold"] += region_units_sold
                region_totals[region_name]["Total Revenue"] += region_total_revenue
            else:
                region_totals[region_name] = {"Units Sold": region_units_sold, "Total Revenue": region_total_revenue}

    # Print title
    print("                           Sales Report")
    print("                           ------------\n")
    print("                      Produced on: {0}\n".format(datetime.datetime.now().strftime("%Y-%m-%d")))

    # Print list of regions
    print("Regions analysed: {0}".format(", ".join(sorted(region_totals.keys()))))

    # Print number of regions
    print("\nTotal, {0} regions.\n".format(len(region_totals)))

    # Print region totals
    for region, totals in sorted(region_totals.items()):
        grant_total_units_sold += totals["Units Sold"]
        grant_total_total_revenue += totals["Total Revenue"]

        print(region)
        print()
        print(" Total units sold:\t\t\t{0}".format(locale.format_string("%d", totals["Units Sold"])))
        print(" Average revenue per unit:\t{0}".format(
            Money(str(totals["Total Revenue"] / totals["Units Sold"]), format_currency).format(format_locale)))
        print(" Total revenue of sales:\t{0}".format(
            Money(str(totals["Total Revenue"]), format_currency).format(format_locale)))
        print()

    # Print grand totals
    print("Grand Totals")
    print()
    print(" Total units sold:\t\t\t{0}".format(locale.format_string("%d", grant_total_units_sold)))
    print(" Average revenue per unit:\t{0}".format(
        Money(str(grant_total_total_revenue / grant_total_units_sold), format_currency).format(format_locale)))
    print(" Total revenue of sales:\t{0}".format(
        Money(str(grant_total_total_revenue), format_currency).format(format_locale)))

except IOError:
    print("There has been an error processing your file.")
    sys.exit(-1)
