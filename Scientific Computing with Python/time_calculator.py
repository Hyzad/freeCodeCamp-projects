def add_time(start, duration, day=False):
    start_all = start.split()
    start_hour = start_all[0].split(":")[0] # starting hour
    start_minute = start_all[0].split(":")[1] # starting minute
    start_a = start_all[1] # starting am or pm
    #print(start_a, start_hour, start_minute)
    add_hour = duration.split(":")[0] # hour that will be added
    add_min = duration.split(":")[1]  # minute that will be added
    ampm = 0 # keeps track of am or pm
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # days of the week
    start_day = 0
  
    if day != False:
        day = day.capitalize()

    if start_a == "PM": # if pm to start with, ampm is 1
        ampm = 1

    minute = int(start_minute) + int(add_min) # stating minutes + the minutes to be added
    #print(minute)

    if minute >= 60: # checks whether minutes are over 60 
        min_remain = minute % 60 # sets the mintutes to the remainder of minute / 60
        min_add = minute // 60 # sets the min_add to the ammount of times minute can be divided by 60
        #print("min", min_remain, min_add)
    else:
        min_add = 0 # no minutes need to be added to the hours
        min_remain = minute # the remaining minutes are less than 60 so they are fine
        #print("min2", min_remain, min_add)

    if len(str(min_remain)) == 1:
        min_remain = "0" + str(min_remain) # checks whether the min_remain is one didget then formats it properly 
        
    
    hour = int(start_hour) + int(add_hour) + min_add # total number of hours
    # print(hour)
    hour_remain = hour

    if hour >= 12:
        hour_remain = hour % 12 # remainer after dividing hour by 12
        ampm = ampm + (hour // 12) # amount of times hour can be divided by 12
        # print("here")
    
    if hour_remain == 0:
        hour_remain = 12

    if ampm % 2 == 0: # if ampm is even it is AM else it is PM
        twelve_hour = "AM" 
    elif ampm % 2 != 0:
        twelve_hour = "PM" 
    #if ampm == 3:
        #return
    #elif ampm > 3:
        #return
    
    if day == "Monday": # assigns a number to each day of the week
        start_day = 1
    elif day == "Tuesday":
        start_day = 2
    elif day == "Wednesday":
        start_day = 3
    elif day == "Thursday":
        start_day = 4
    elif day == "Friday":
        start_day = 5
    elif day == "Saturday":
        start_day = 6
    elif day == "Sunday":
        start_day = 7
    
    day_change = ampm // 2
    # print(day_change)

    day_fin = ""
    if day != False:
        end_day = ((day_change + start_day) % 7) - 1
        day_fin = ", " + days[end_day]
    

    day_text = ""
    if day_change == 1:
        day_text = " (next day)"
    if day_change >= 2:
        day_text = (f" ({day_change} days later)") 
    new_time = (str(hour_remain) + ":" + str(min_remain) +
                " " + twelve_hour + day_fin + day_text)
    # print("ampm:", ampm)
    return new_time