# I can't import libraries :(
import re

arg1 = "11:00 PM"
arg2 = "200:10"
arg3 = "Sunday"

regex1 = r"(\d+):(\d+) (AM|PM)"
match1 = re.match(regex1, arg1)

if match1:
    ori_hours = int(match1.group(1))
    ori_mins = int(match1.group(2))
    meridian = match1.group(3)
    print("ori_hours:", ori_hours, "ori_mins:", ori_mins, "meridian:", meridian, "day", arg3)

regex2 = r"(\d+):(\d+)"
match2 = re.match(regex2, arg2)

if match2:
    add_hours = int(match2.group(1))
    add_mins = int(match2.group(2))
    print("add_hours", add_hours, "add_mins", add_mins)

add_days, final_add_hours = divmod(add_hours, 12)

# New mins

new_mins = ori_mins + add_mins

if (new_mins) >= 60:
    add_hours += 1
    new_mins -= 60
print("new_mins", new_mins)

# New hours, need while loop to account for multiples of 12

new_hours = ori_hours + add_hours

while new_hours > 12:

    if meridian == "AM":
        new_hours -= 12
        meridian = "PM"
    elif meridian == "PM":
        new_hours -= 12
        add_days += 1
        meridian = "AM"

days_later = add_days

print("new_hours:", new_hours, "add_days", add_days, "meridian", meridian)

# New weekday if sought
if arg3:
    week_days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    # Function for finding current key
    def get_key_for_value(d, value_to_find):
        for key, value in d.items():
            if value == value_to_find:
                return key
        return None

    new_key = (get_key_for_value(week_days, arg3) + (add_days % 7)) % 7

    new_day = week_days[new_key]

    print("new_day", new_day)
# If weekday not given and sought

if days_later == 1:
    print("next day")
elif days_later > 1:
    print(days_later, "days later")

  