#!/usr/bin/python
# Show the expenses for this year

from util.list import text_to_table, table_to_text

#-----------------------------------------------------------------------------
# Replacer

from re             import match
# match('.*Unit(30\d\d).*(20\d\d-\d\d-\d\d).*', path)

substitutions = [
    [ 'WME', 'Watermill' ],
    [ 'ONLINE TRANSFER .* BUSINESS MARKET RATE SAVINGS.*', 'Transfer Savings' ],
    [ 'BUSINESS CARD', 'Business Visa card' ],
    [ 'ONLINE TRANSFER TO SEAMAN', 'Paycheck for Bryan' ],
    [ '.*TO BUSINESS CARD.*', 'Pay business Visa'],
    [ '.*SWARMA.*', 'Web Faction'],
    [ 'DEPOSIT', 'Deposit pay' ],
    [ 'PAYPAL', 'Pay pal - ISP payments' ],
    [ 'CANONICAL', 'Canonical - ISP payments' ],
    [ 'HOSTGATOR.COM.*', 'Host Gator' ],
    [ '.*GITHUB', 'Git Hub - ISP payments' ],
]

# Find all replacement in row
def subst_row(row):
    for s in substitutions:
        if match(s[0], row[1]):
            return row[:1] + [ s[1] ] + row[2:]
    return row

# Subst all rows
def substitute(table):
    return [ subst_row(row) for row in table ]

#-----------------------------------------------------------------------------
# Create the table

total = 0

# Create CSV for each row
def create_row_semicolons(row):
    global total
    if len(row)<5:  return [ row[0],'',0,'' ]
    value = float(row[1].replace(',','').strip())
    total += value
    return [ row[0].strip(), row[4].strip(), value, '' ]

# Read fixed columns of each row
def create_row_columns(row):
    global total
    if len(row[2])<3: return [ row[0],'',0,'' ]
    value = float(row[2].replace(',','').strip())
    total += value
    return [ row[0].strip(), row[1].strip(), value, '' ]

# Create the correct table for the input type
def create_table(text, sep=';',rows=create_row_semicolons):
    table = text_to_table(text,sep)
    table = map(rows,table)
    table = filter(lambda x:x[2]!=0, table)
    table = substitute(table)
    return table

#-----------------------------------------------------------------------------
# File readers

# Read the bank data
def read_semicolon_file(f,):
    text = open(f).read()
    return create_table(text)

# Read the bank data
def read_columns_file(f):
    text = open(f).read()
    return create_table(text,'x',create_row_columns)

def negative(x):
    return [ x[0],x[1],-x[2],x[3] ]

# Select all of the expense transactions
def select_expenses(table):
    table = filter(lambda x:x[2]<0, table)
    return map(negative, table)

# Select all of the income transactions
def select_income(table):
    return filter(lambda x:x[2]>0, table)

    
#-----------------------------------------------------------------------------
# File writers

# Format one output row
def format_row(row):
    if len(row[0])<6 :
        return "%s,%s,%4.2f,%s" % (row[0]+'/2013',row[1],row[2],row[3])
        #return "%s,%-40s,%4.2f,%10s" % (row[0]+'/2013',row[1],row[2],row[3])
    return "%s,%s,%4.2f,%s" % (row[0],row[1],row[2],row[3])
    #return "%s,%-40s,%4.2f,%10s" % (row[0],row[1],row[2],row[3])

# Print the table
def print_report(table):
    text = '\n'.join(map(format_row, table))
    return text

# Print the table
def save_report(f, text):
    open(f, 'w').write(text+'\n')
