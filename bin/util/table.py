#!/usr/bin/env python
from date  import date_str,to_date
from csv   import writer, reader

from files import write_file


# Create some imaginary data to work with
def create_data(num_rows=10, num_columns=10):
    return [ [ 0+c+row*100 for c in range(num_columns) ]+[ row ] for row in range(num_rows) ]


#############################################################################
# CSV files

# Export a list of lists to a text file
def export_csv (csvfile,table):
    with open(csvfile, 'w') as f:
        w = writer(f)
        for row in table:
            w.writerow(row)

# Import rows of text and make a list of lists
def import_csv(csvfile):
    with open(csvfile) as f:
        return [ x for x in reader(f) ]

# Convert strings to ints
def int_row(row):
    return map(int, row)

def int_table(table):
    return map(int_row, table)

#############################################################################
# Query tables

# Print a table of rows and columns
def print_table(table):
    for r in table:
        for i in r:
            print i,
        print

# Format a table row as a single string
def row_as_text(row):
     lst = map(str,row)
     return ",".join(lst)

# Save a table as a CSV file
def save_table(filename, table):
     write_file(filename, map(row_as_text, table))
          
#############################################################################
# Differences

# Calculate the difference between two rows
def row_diffs(x,y):
    return [ a[1]-a[0] for a in zip(x[2:],y[2:]) ]

# Extract the fixed part of the row
def row_head(x):
    return x[0:2]

# Build a new row to hold the diffs
def difference_row (x,y):
    return row_head(y)+row_diffs(x, y)

# Calculate the new array of difference rows
def calculate_differences(data):
    return [  difference_row(data[i], data[i+1]) for i in range(len(data)-1) ]

##################################################################
# Gallons


# Calculate the difference between two rows
def row_multiply(x,y):
    return [ a[1]*a[0] for a in zip(x[2:],y[2:]) ]

# Extract the fixed part of the row
def row_head(x):
    return x[0:2]

# Build a new row to hold the diffs
def summarize_row (x,y):
    return row_head(y)+row_multiply(x, y)

# Return the sum of a list of numbers
def sum(numbers):
     return reduce(lambda x,y:x+y, numbers)

# Multiply values in two vectors
def multiply(v1,v2):
     return [ a[1]*a[0] for a in zip(v1,v2) ]

# Multiply the elements and return the sum
def value_of(v1,v2):
     return sum (multiply (v1,v2))

##################################################################
# Daily totals

# Check to see if to times are in the same day
def same_day(d1, d2):
    return date_str(d1)==date_str(d2)

# Calculate the new array of difference rows
def calculate_daily(data):
    daily_base = data[0]
    result = []
    for i in range(len(data)-1):
        if not same_day(daily_base[1], data[i][1]): 
            daily_base = data[i]
        result.append (difference_row (daily_base, data[i+1]))
    return result
