d1=[11,3,2006]
d2=[11,1,2006]
day31=[1,3,5,7,9,11]
day30=[4,6,8,10,12]
def leap(d):
    while d[2]/10!=0:
        if d[2]%4==0:
            return 29
        else :
            return 26

def days(d1,d2):

    years=d1[2]-d2[2]
    days1=d1[0]
    days2=d2[0]
    while d1[1]!=0 :
        if d1[1] in day30:
            days1=days1+30
        elif d1[1]==2:
            days1+=leap(d1)
        elif d1[1] in day31 :
            days1=31+d1[0]+days1
        print(d1[1]-1)
        d1[1]=d1[1]-1

        print(days1)
    d1[2] = d1[2] - 1
    while d2[1]!=13:
        if d2[1] in day30:
            days2= days2 +30
        elif d2[1] in day31:
            days2=31+d2[0]+days2
        print(d2[1] + 1)
        d2[1] = d2[1] +1
        print(days2)
d2[2]=d2[2]-1
if d1[2]<d2[2]:
    days(d1,d2)
else:
    days(d2,d1)
