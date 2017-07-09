month_name_arr = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] + 7  * ['th'] \
        + ['st']

year = input("Year: ")
month= input("Month: ")
day =  input("Day: ")

month_number = int(month)
day_number = int(day)

month_name = month_name_arr[month_number -1]
day_name = day + endings[day_number - 1]

print("Date is: " + month_name +" "+ day_name + " " + year )