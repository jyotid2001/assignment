import datetime

#days in month function
def days_in_month(year, month):
#computing number of days in a month
  if (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1 <= month <=11):
     date1 = datetime.date(year, month, 1)
     date2 = datetime.date(year, month+1, 1)
     return (date2 - date1).days
  elif (datetime.MINYEAR <= year <= datetime.MAXYEAR) and (month == 12):
     date1 = datetime.date(year, month, 1)
     date2 = datetime.date(year+1, 1, 1)
     return (date2 - date1).days
  else:
     return False

#date is valid function
def is_valid_date(year, month, day):
 #computing date is valid or not
 days = days_in_month(year, month)
 if ((datetime.MINYEAR <= year <= datetime.MAXYEAR) and (1<= month <= 12) and (0 < day <= days)):
  return True
 else:
  return False

#computing number of days between two dates
def days_between(year1, month1, day1, year2, month2, day2):
 #computing the number between days
 #conditions and computation of days between two dates
 if (is_valid_date(year1, month1, day1)) and (is_valid_date(year2, month2, day2)):
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    if (date2 > date1):
     number_of_days = date2 - date1
     return number_of_days.days
    else:
     return 0
 else:
    return 0


#computing person's age in days
def age_in_days(year, month, day):
#conditions and calculations of person's age in days
 if (is_valid_date(year, month, day)):
  today = datetime.date.today()
  person_bday = datetime.date(year, month, day)
  if (person_bday < today):
     person_age_in_days = days_between(year, month, day, today.year, today.month, today.day)
     return person_age_in_days
  else:
     return 0
 else:
   return 0
year_input = int(input("Please write the year you want to calculate"))
month_input = int(input("Please give the number of the month"))
print("Total Days in Month is :", days_in_month(year_input, month_input))

# Add the year, month, day for parts 1
year_input1 = int(input("Please write the year you want to check"))
month_input1 = int(input("Please give the number of the month for finalise checking"))
day_input1 = int(input("Please give the date for Checking"))
print("Given date is :", is_valid_date(year_input1, month_input1, day_input1))

# Add the year, month, day for parts 2
year_input2 = int(input("Please write the year from where you want to calculate"))
month_input2 = int(input("Please write the month from where you want to calculate"))
day_input2 = int(input("Please write the date from where you want to calculate"))

# Add the year, month, day for parts 3
year_input3 = int(input("Please write the end year where you want to calculate"))
month_input3 = int(input("Please write the end of the month where you want to calculate"))
day_input3 = int(input("Please write the end date where you want to calculate"))
print("Distance Between The Given Dates :", days_between(year_input2, month_input2,
day_input2, year_input3, month_input3, day_input3))

# Add the year, month, day for parts 4
year_input4 = int(input("Please write the year of birth"))
month_input4 = int(input("Please write the month of birth"))
day_input4 = int(input("Please write the date of birth"))
print("Persons age in days :", age_in_days(year_input4, month_input4, day_input4))






##Please write the year you want to calculate 2021
##Please give the number of the month 4
##Total Days in Month is : 30
##Please write the year you want to check 2020
##Please give the number of the month for finalise checking 4
##Please give the date for Checking 12
##Given date is : True
##Please write the year from where you want to calculate 2020
##Please write the month from where you want to calculate10
##Please write the date from where you want to calculate1
##Please write the end year where you want to calculate2021
##Please write the end of the month where you want to calculate 10
##Please write the end date where you want to calculate 1
##Distance Between The Given Dates : 365
##Please write the year of birth 2001
##Please write the month of birth 12
##Please write the date of birth 21
##Persons age in days : 7134
