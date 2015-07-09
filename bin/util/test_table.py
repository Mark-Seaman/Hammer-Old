from util.table import export_csv, import_csv, int_table, print_table, create_data


# Create a table and read and write it
def test_create_data():
    table  = create_data(20,5)
    assert(len(table)==20)
    table  = create_data()
    assert(len(table)==10)
    table  = create_data(20)
    assert(len(table)==20)
    table  = create_data(20,num_columns=9)
    assert(len(table)==20 and len(table[9])==10)


# Create a table and read and write it
def test_write_csv():
    table  = create_data(20,5)
    tmp = '/tmp/data.csv'
    export_csv(tmp, table)


# Read a table from a file
def test_read_csv():
    table1  = create_data(20,5)
    table2 = import_csv('/tmp/data.csv')
    assert(len(table1)==len(table2))
    assert(table1==int_table(table2))


# Print the table
def test_print():
    print_table (import_csv('/tmp/data.csv'))

# Convert a table to itegers
def test_int_table():
    s = str(int_table(import_csv('/tmp/data.csv')))
    x = '[[0, 1, 2, 3, 4, 0], [100, 101, 102, 103, 104, 1], [200, 201, 202, 203, 204, 2], [300, 301, 302, 303, 304, 3], [400, 401, 402, 403, 404, 4], [500, 501, 502, 503, 504, 5], [600, 601, 602, 603, 604, 6], [700, 701, 702, 703, 704, 7], [800, 801, 802, 803, 804, 8], [900, 901, 902, 903, 904, 9], [1000, 1001, 1002, 1003, 1004, 10], [1100, 1101, 1102, 1103, 1104, 11], [1200, 1201, 1202, 1203, 1204, 12], [1300, 1301, 1302, 1303, 1304, 13], [1400, 1401, 1402, 1403, 1404, 14], [1500, 1501, 1502, 1503, 1504, 15], [1600, 1601, 1602, 1603, 1604, 16], [1700, 1701, 1702, 1703, 1704, 17], [1800, 1801, 1802, 1803, 1804, 18], [1900, 1901, 1902, 1903, 1904, 19]]'
    assert (s==x)
