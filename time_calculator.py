def add_time(start, duration, starting_day=""):
    # Separte the start into hours and minutes
    Parts = start.split()
    time = Parts[0].split(":")
    ampm = Parts[1]

    # Calculate 24-hour clock format
    if ampm == "PM" :
        hour = int(time[0]) + 12
        time[0] = str(hour)
    
    # Separate the duration into hours and minutes
    DurParts = duration.split(":")

    # Add hours and minutes
    HourSum = int(time[0]) + int(DurParts[0])
    MinSum = int(time[1]) + int(DurParts[1])

    if MinSum >= 60 :
        hours_add = MinSum // 60
        MinSum -= hours_add * 60
        HourSum += hours_add

    AddDays = 0
    if HourSum > 24 :
        AddDays = HourSum // 24
        HourSum -= AddDays * 24
    
    # Find AM and PM
    # Return to 12-hour clock format
    if HourSum > 0 and HourSum < 12 :
        ampm = "AM"
    elif HourSum == 12 :
        ampm = "PM"
    elif HourSum > 12 :
        ampm = "PM"
        HourSum -= 12
    else : # HourSum == 0
        ampm = "AM"
        HourSum += 12

    if AddDays > 0 :
        if AddDays == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(AddDays) + " days later)"
    else :
        days_later = ""

    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if starting_day :
        weeks = AddDays // 7
        i = week_days.index(starting_day.lower().capitalize()) + (AddDays - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + week_days[i]
    else :
        day = ""
    
    new_time= str(HourSum) + ":" + \
        (str(MinSum) if MinSum > 9 else ("0" + str(MinSum))) + \
        " " + ampm + day + days_later
    
    return new_time