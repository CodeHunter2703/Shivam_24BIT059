def leap_year(year):
     if (year%400==0):
         return True
     else:
         return False
date_leap={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
date_notleap={**date_leap,2:28}
def datediff(date1,date2):
    if date2 < date1:
        date1,date2=date2,date1
        print(date1,date2)
    d1 , m1 , y1=date1
    d2 , m2 , y2 = date2
    total_days=0

    total_days=d1+d2
    print(total_days)
    d1,d2=0,0
    print(date1 != date2)
    while date1 != date2 :
        print( leap_year(y1))
        if leap_year(y1):
            total_days+=date_leap[m1]
        else:
            total_days+=date_notleap[m1]
        print(m1, total_days)
        m1+=1

        if m1 > 12:
            m1=1
            y1+=1
    return total_days
result=datediff([3,4,2024],[2,4,2024])
print(result)
