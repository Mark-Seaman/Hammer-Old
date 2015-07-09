#!/usr/bin/python
# Show the expenses for this year

from sys import argv

# Read text into an array of lines
def read_file(f):
    return  [line[:-1] for line in open(f).readlines()]

# Split each line into columns
def create_table(text):
    return map (lambda x: x.split(','), text)  

# Select the transactions with three columns
def select_transactions(rows):
     return filter(lambda x: len(x)==3, rows)    

# Join the columns of text with tabs to form one row
def format_row(row):
    row = map(lambda x: '"'+x+'"', row)
    return ','.join(row)

# Join row together as text
def format_table(table):
    rows = sorted(map(format_row, table))
    return '\n'.join (rows)

# Remove any extra spaces
def read_dollar_value(row):
    return float(row[2].strip())

# Calculate the total, number of transaction, and average
def calculate_summary(table):
    expenses = map (read_dollar_value, table)
    total =  reduce (lambda x,y: x+y, expenses)
    average = total/len(expenses)    
    return [total, len(expenses), average]

# Print a summary of the expenses
def summary(stats):
    return "\n\n\"Total = $%4.2f,  " % stats[0]+\
         "%d transactions,  " % stats[1]+\
        '$%4.2f average\"\n' % stats[2]

# Create a title line 
def title(filename):
    return '"%s"\n\n' % filename.replace('.csv','')

# Print a table of row and columns
def write_table(filename, table):
    text =  title(filename) + format_table(table) + summary(calculate_summary(table))
    open(filename,'w').write(text)

# Process all text in a known file
def create_expense_listing(f,output):
    table = read_file(f)
    table = create_table(table)
    table = select_transactions(table)
    write_table(output, table)
