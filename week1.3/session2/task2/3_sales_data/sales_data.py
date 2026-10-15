# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

with open("sales.csv", "r") as sales:
    rows = sales.readlines()
    
    #largets sale day
    current = -1
    largest_day = ""
    total_sales_amount = 0
    for i in range(1, len(rows)):
        items = rows[i].split(",")

        #sales amount - column 3
        #date - column1
        if (int(items[2]) > current):
            current = int(items[2])
            largest_day = items[0]

        #average sale amount
        total_sales_amount += int(items[2])

        
    print("Latest date with the largest sale amount:", largest_day)
    print("Average sales amount:", total_sales_amount / (len(rows)- 1))

    



# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows