#!/usr/bin/python

from sys        import stdin
from datetime   import datetime, timedelta
from string     import strip

# Read lines from a file and strip off the tailing newline
def read_file(f):
    results = [line[:-1] for line in f.readlines()]
    f.close()
    return results

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
    if to_time(t2) >= to_time(t1):
        return str(to_time(t2)-to_time(t1))
    else:
        return "-"+str(to_time(t1)-to_time(t2))  

# List the minutes
def minutes(t):
    return to_time(t).minute + to_time(t).hour*60

# Sum up a list of individual times
def sum_time(time_list):
    total = 0
    for t in time_list:
        total += minutes(t)
        #print t, "%d:%d"%(total/60, total%60)
    return total

# Print out a summary of the hours and pay
def print_summary(time_list,rate):
    total_minutes = sum_time(time_list)
    days = len(time_list)
    print '    Work days:    ', days
    print '    Average hours: %4.2f'%(total_minutes/60.0/days)
    print "    Total time:    %d:%02d"%(total_minutes/60, total_minutes%60)
    if rate:
        print "    Total hours:   %4.2f"%(total_minutes/60.0)
        print "    Rate:          $%d/hour"%rate
        print "    Amount due:    $%4.2f"%(total_minutes/60.0*rate)


#____________________________________________________
# Work Time
#____________________________________________________
    
# Print the difference in time for two sessions
def print_work_time(parts):
    print "%-3s %-6s %-40s %s"%(parts[0]+',', strip(parts[1])+',', strip(parts[2])+',', strip(parts[3]))

# Print out each day and the time worked
def print_time_sheet(days,rate=None):
    time_list = []
    for day in days:    
        # print "...", day, "..."
        parts = day.split (',')

        if len(parts)==4:
            print_work_time (parts)
            time_list.append(strip(parts[3]))
        else:
            if len(strip(day))>1: 
                print "**"
            print day
    print_summary(time_list,rate)
  

# Total all the time entries
def time_summary():
    time_text = stdin.read().split('\n')
    print_time_sheet(time_text)
