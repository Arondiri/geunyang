def date_time(time: str) -> str:
    time = time.split('.')
    time[2] = time[2].split(' ')
    time[2][1] = time[2][1].split(':')
    M = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if int(time[2][1][0]) == 1 and int(time[2][1][1]) != 1:
        return str(int(time[0]))+' '+M[int(time[1])-1]+' '+str(int(time[2][0]))+' year '+str(int(time[2][1][0]))+' hour '+str(int(time[2][1][1]))+' minutes'
    elif int(time[2][1][0]) != 1 and int(time[2][1][1]) == 1:
        return str(int(time[0]))+' '+M[int(time[1])-1]+' '+str(int(time[2][0]))+' year '+str(int(time[2][1][0]))+' hours '+str(int(time[2][1][1]))+' minute'
    elif int(time[2][1][0]) == 1 and int(time[2][1][1]) == 1:
        return str(int(time[0]))+' '+M[int(time[1])-1]+' '+str(int(time[2][0]))+' year '+str(int(time[2][1][0]))+' hour '+str(int(time[2][1][1]))+' minute'
    elif int(time[2][1][0]) != 1 and int(time[2][1][1]) != 1:
        return str(int(time[0]))+' '+M[int(time[1])-1]+' '+str(int(time[2][0]))+' year '+str(int(time[2][1][0]))+' hours '+str(int(time[2][1][1]))+' minutes'
