def bisiesto2(n):
    r=0
    if(n%4==0):
        if(n%100!=0 or n%400==0):
            return r