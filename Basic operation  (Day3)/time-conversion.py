total_seconds = int(input("Time in second:"))
hours = 0
minutes = 0
seconds = 0
if total_seconds < 0:
    print("please !! enter postive number")
elif total_seconds < 60:
    seconds = total_seconds
    print(hours,"hours",minutes,"minutes",seconds,"seconds")
else:
    if total_seconds >= 3600:
        hours = total_seconds // 3600
        total_seconds = total_seconds % 3600

    if total_seconds >= 60:
        minutes = total_seconds // 60
        total_seconds = total_seconds % 60

    if total_seconds < 60:
        seconds = total_seconds

    #result
    print(hours,"hours",minutes,"minutes",seconds,"seconds")
