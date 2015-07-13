from re    import match

#-----------------------------------------------------------------------------
# Unique items

# Select the unique items from a list
def unique (lst):
   return [ i for i in set(item for item in lst) ]

# Count unique instances of items in a list
def count_unique (dupedList):
   uniqueSet = set(item for item in dupedList)
   return [(item, dupedList.count(item)) for item in uniqueSet]

#-----------------------------------------------------------------------------
# Columns

# Convert a list into a CSV string (,)
def list_to_csv(lst):
     return ','.join(map(str,lst))

# Convert a list into a CSV string  (;)
def list_to_ssv(lst):
     return ';'.join(map(str,lst))

# Convert CSV string into a list
def record_list(string):
   l = csv_to_list(string)
   return l[:2]+map(int,l[2:])

# Convert CSV string into a list
def csv_to_list(string):
     return string.split(',')

# Convert CSV string into a list
def ssv_to_list(string):
     return string.split(';')

# Extract fixed columns from line of text
def columns_to_list(string):
   return [ string[0:6], string[30:75],string[76:8420] ]
   

#-----------------------------------------------------------------------------
# Rows

# Join lines of text to create a string
def join_lines(lines):
   return '\n'.join(map(str,lines))+'\n'

# Split up a block of text into lines
def split_lines(text):
   return text.split('\n')

#-----------------------------------------------------------------------------
# Tables

# Filter empty lines
def remove_empty_lines(lines):
   return filter(lambda x: not match(r'^\s*$', x), lines)

# Filter comment lines (lines that start with #)
def remove_comment_lines(lines):
   return filter(lambda x: not match(r'^\s*#.*$', x), lines)


# Split the lines of text
def csv_lines_to_table(text):
   return map(csv_to_list, text)


# Convert text to a table
def text_to_table(text,sep=','):
   if sep==',':
      return map(csv_to_list, split_lines(text))
   if sep==';':
      return map(ssv_to_list, split_lines(text))
   return map(columns_to_list,split_lines(text))


# Convert table to text
def table_to_text(table,sep=','):
   if sep==',':
      table = map(list_to_csv, table)
      return join_lines(table)
   if sep==';':
      table = map(list_to_ssv, table)
      return join_lines(table)
   return join_lines(table)
