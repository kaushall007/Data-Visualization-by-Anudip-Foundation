seconds = int(input("Time in Second:"))

hours = 0
minutes = 0
remaining_seconds = seconds
if seconds < 60:
    print(seconds,"sec")
else:

    # Calculate hours if total seconds are more than 3600
    if seconds >= 3600: 
        hours = seconds % 3600
        
    # Calculate minutes if remaining seconds are more than 60
    if remaining_seconds >= 60:
        minutes = remaining_seconds // 60
        remaining_seconds = remaining_seconds % 60
        
    # The remaining seconds are the final seconds
    seconds = remaining_seconds

    print(hours,"hr", minutes,"min", seconds,"sec")

