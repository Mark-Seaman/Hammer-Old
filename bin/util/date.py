#!/usr/bin/python

from re             import match
from datetime       import datetime, date, timedelta 


# Convert a date from string to date object
def string_to_date(str_date):
    m = match(r'(20\d\d)-(\d\d)-(\d\d)', str_date)
    return date(year=int(m.group(1)), month=int(m.group(2)), day=int(m.group(3)))

# Return a date from eight days ago
def last_week(date):
    return  str(date-timedelta(days=8))

# Return a date from 48 hours ago
def two_days_ago(date):
    return  str(date-timedelta(days=2))

# Get the string for the date from one day previous
def str_yesterday(str_date):
    return  str(string_to_date(str_date)-timedelta(days=1))

# Return a date for yesterday
def yesterday(date):
    return  str(date-timedelta(days=1))

#____________________________________________________
# Time
#____________________________________________________

# Convert from string to seconds after 1970
def to_time(s):
     return datetime.strptime(s, "%H:%M")

# Convert from a time record to string
def time_str(t):
    return t.strftime("%H:%M")

# Return time now as a string
def now_str():
    return time_str(datetime.now())  

# Format the elapsed time
def elapsed(t1,t2):
    if t2 >= t1:
        return str(to_time(t2)-to_time(t1))
    else:
        return "-"+str(to_time(t1)-to_time(t2))     

#____________________________________________________
# Date
#____________________________________________________

# Convert from string to seconds after 1970
def to_date(s):
     return datetime.strptime(s, "%Y-%m-%d")

# Convert from a time record to string
def date_str(t):
    return t.strftime("%Y-%m-%d")

# Format like   Tue, 03-11
def day_str(t):
    return t.strftime("%a, %m-%d")

# Format with time
def date_str_with_time(t):
    return t.strftime("%Y-%m-%d-%H-%M")

# Return date today as a string
def today_str():
    return date_str(datetime.today())  

# Return this date yesterday as a string
def yesterday_str():
    return date_str(to_date(today_str())-timedelta(days=1)) 

# Return this date yesterday as a string
def someday_str(days):
    return day_str(to_date(today_str())+timedelta(days=days)) 


#____________________________________________________
# Date & Time
#____________________________________________________

# Convert a date from date object to string 
def date_time_str(str_date_time, format="%Y-%m-%d-%H:%M:%S"):
    return datetime.strftime(str_date_time, format)

# Convert from string to seconds after 1970 (return the datatime object)
def to_date_time(string, format="%Y-%m-%d-%H:%M:%S"):
     return datetime.strptime(string, format)


# Convert a date from string to date object
def wm_string_to_time(str_date):
    str_date = fix_date(str_date)
    return datetime.strptime(str_date,"%Y%m%d-%H:%M:%S")
def time_to_wm_string(time):
     return time.strftime("%Y%m%d-%H:%M:%S")


# Create valid file names
def filename_time_string(time=datetime.now()):
    return date_time_str (time, "%Y-%m-%d_%H%M")
def filename_string_time(string):
     return to_date_time(string, "%Y-%m-%d_%H%M")

# Function to test if a string is a Watermill formatted string
def is_wm_date_string(s):
    return (len(s) > 15 and s[0] == '2' and s[1] == '0' and s[8]== '-')

# Funcion to test if a sring is YYYY-MM-DD or YY-MM-DD-hh-mm formatted
def is_YYYY_MM_DD_date_string(s):
    if not s.startswith('201'):
        return False
    if (len(s) == 10) and s[4] == '-' and s[7] == '-' : 
        return True
    if (len(s) == 16) and s[4] == '-' and s[7] == '-' and s[10] == '-' and s[13] == '-' : 
        return True
    return False

def convert_YYYY_MM_DD_to_time(str_date):
    if len(str_date) == 16:
        return datetime.strptime(str_date,"%Y-%m-%d-%H-%M")
    if len(str_date) == 10:
        return datetime.strptime(str_date,"%Y-%m-%d")
    return "<DATE_ERR>"

#____________________________________________________
# Fix the string if it is formatted as a new watermill date

def fix_date(s):
    if s[11]==':': return s
    return s[:11]+':'+s[11:13]+':'+s[13:15]+s[19:]

def test_fix_date():
    s1 = '20110628-23:14:00,40,31,147,38,26,48,50,50,3'
    assert(s1==fix_date(s1))
    s3 = '20130212-150000.167,0,0,0,0,0,0,1,1,3'
    s4 = '20130212-15:00:00,0,0,0,0,0,0,1,1,3'
    print s3
    print fix_date(s3)
    assert(s4==fix_date(s3))

