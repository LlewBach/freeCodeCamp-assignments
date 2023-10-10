def add_time(start, duration, day=None):

    def parse_time(time_string):
        # Remove spaces
        time_string = time_string.replace(" ", "")
        # Split around colon
        parts = time_string.split(":")
        # Extract hour
        hours = int(parts[0])
        # Extract mins and meridian
        if "AM" in time_string or "PM" in time_string:
            mins = int(parts[1][:-2])
            meridian = parts[1][-2:]
        else:
            mins = int(parts[1])
            meridian = None
        
        return hours, mins, meridian
    
    ori_hours, ori_mins, meridian = parse_time(start)

    add_hours, add_mins, ignore = parse_time(duration)

    # New mins

    new_mins = ori_mins + add_mins

    if (new_mins) >= 60:
        add_hours += 1
        new_mins -= 60

    # New hours, need while loop to account for multiples of 12

    new_hours = ori_hours + add_hours
    days_later = 0

    while new_hours > 12:
        if meridian == "AM":
            new_hours -= 12
            meridian = "PM"
        elif meridian == "PM":
            new_hours -= 12
            days_later += 1
            meridian = "AM"

    if new_hours == 12:
        if meridian == "AM":
            meridian = "PM"
        elif meridian == "PM":
            days_later += 1
            meridian = "AM"

    # Converting integers back to double digit strings
    new_mins = str(new_mins).zfill(2)
    new_hours = str(new_hours).zfill(2)

    # Return statement if no days added and no day sought
    if not days_later and not day:
        return f"{new_hours}:{new_mins} {meridian}"

    # Return statement if no days added but day sought
    if not days_later and day:
        return f"{new_hours}:{new_mins} {meridian}, {day}"

    # Return statement if days added but no day sought
    if days_later and not day:
        if days_later == 1:
            return f"{new_hours}:{new_mins} {meridian} (next day)"
        else:
            return f"{new_hours}:{new_mins} {meridian} ({days_later} days later)"
        

    # Finding new weekday
    if day:
        week_days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }

        # Function for finding current key
        def get_key_for_value(d, value_to_find):
            for key, value in d.items():
                if value == value_to_find:
                    return key
            return None
        

        new_key = (get_key_for_value(week_days, day) + (days_later % 7)) % 7

        new_day = week_days[new_key]

        if days_later == 1:
            return f"{new_hours}:{new_mins} {meridian}, {new_day} (next day)" 
        else:
            return f"{new_hours}:{new_mins} {meridian}, {new_day} ({days_later} days later)"
    

print(add_time("11:30 AM", "2:32", "Monday"))