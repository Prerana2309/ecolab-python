def week_day_name(index):
    if index==0: return "Sunday"
    elif index==1: return "Monday"
    elif index==2: return "Tuesday"
    elif index==3: return "Wednesday"
    elif index==4: return "Thursday"
    elif index==5: return "Friday"
    elif index==6: return "Saturday"

def is_leap_year(year):
    return (year%100!=0 and year%4==0) or year%400==0

def days_in_month(month , year=1990):
    if month==2:
        return 28+int(is_leap_year(year))        
    elif (month<8 and month%2!=0) or (month>=8 and month%2==0):
        return 31
    else:
        return 30


def date_value(day ,month, year):
    value=0
    y=year-1
    value = y * 365 + y//4  - y//100 + y//400

    m=1
    while m<month:
        value+= days_in_month(m,year)
        m+=1

    value+=day
    return value

def date_to_week_day(date,month,year):
    ref_date = date_value(1,1,2006)
    input_date= date_value(date,month,year)
    diff= (input_date-ref_date) % 7
    return diff

def day_name(index):
    day_names=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
    return day_names[index]

def date_to_day_name(date,month,year):
    diff=date_to_week_day(date,month,year)
    return day_name(diff)

def print_calendar_vertical(month,year):
    startdate=date_to_week_day(1,month,year)
    days=days_in_month(month,year)
    week=['Sun','Mon','Tue','wed','thu','fri','Sat']
    for i in week:
        print(week, end="\n")
        
    
    
#print(print_calendar_vertical(9,2023))