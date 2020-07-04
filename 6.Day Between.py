def days_diff(a, b):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    B = [31,28,31,30,31,30,31,31,30,31,30,31]
    C = [31,29,31,30,31,30,31,31,30,31,30,31]
    c = 0
    if a[0] == b[0] and a[1] == b[1]:
        return abs(a[2]-b[2])
    elif a[0] == b[0] and a[1] != b[1]:
        if a[1] > b[1]:
            return a[2]-b[2]+sum(B[A.index(b[1]):A.index(a[1])])
        elif a[1] < b[1]:
            return b[2]-a[2]+sum(B[A.index(a[1]):A.index(b[1])])
    else:
        if a[0] > b[0]:
            for i in range(1,a[0]-b[0]):
                if ((b[0]+i)%4 == 0 and (b[0]+i)%100 != 0) or (b[0]+i)%400 == 0:
                    c += 366
                else:
                    c += 365
            if (b[0]%4 == 0 and b[0]%100 != 0) or b[0]%400 == 0:
                c += C[A.index(b[1])]-b[2]+sum(C[A.index(b[1])+1:12])+1
            else:
                c += B[A.index(b[1])]-b[2]+sum(B[A.index(b[1])+1:12])+1
            if (a[0]%4 == 0 and a[0]%100 != 0) or a[0]%400 == 0:
                c += a[2]-1+sum(C[0:A.index(a[1])])
            else:
                c += a[2]-1+sum(B[0:A.index(a[1])])
            return c
        elif a[0] < b[0]:
            for i in range(1,b[0]-a[0]):
                if ((a[0]+i)%4 == 0 and (a[0]+i)%100 != 0) or (a[0]+i)%400 == 0:
                    c += 366
                else:
                    c += 365
            if (a[0]%4 == 0 and a[0]%100 != 0) or a[0]%400 == 0:
                c += C[A.index(a[1])]-a[2]+sum(C[A.index(a[1])+1:12])+1
            else:
                c += B[A.index(a[1])]-a[2]+sum(B[A.index(a[1])+1:12])+1
            if (b[0]%4 == 0 and b[0]%100 != 0) or b[0]%400 == 0:
                c += b[2]-1+sum(C[0:A.index(b[1])])
            else:
                c += b[2]-1+sum(B[0:A.index(b[1])])
