def sun_angle(time):
    time = time.split(':')
    for i in range(len(time)):
        time[i] = int(time[i])
    if time[0] < 6 or (time[0] >= 18 and time[1] > 0):
        return "I don't see the sun!"
    else:
        return ((((time[0]-6)*60+time[1])*18000)//(12*60))/100
