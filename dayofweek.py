import sys
#Codes to be used to calculate day of the week
yeardict=({'00':'0','01':'1','02':'2','03':'3','04':'5','05':'6','06':'7',
               '07':'8','08':'3','09':'4','10':'5','11':'6','12':'1',
               '13':'2','14':'3','15':'4','16':'6','17':'7','18':'8',
               '19':'9','20':'4','21':'5','22':'6','23':'7','24':'2',
               '25':'3','26':'4','27':'5','0':'0','1':'1','2':'2','3':'3',
               '4':'5','5':'6','6':'7','7':'8','8':'3','9':'4'})
centurydict=({'16':'0','17':'5','18':'3','19':'1'
               ,'20':'0','21':'5','22':'3','23':'1','24':'0','25':'5'
               ,'26':'3','27':'1'})
monthdict=({'01':'6','02':'2','03':'2','04':'5','05':'0','06':'3',
               '07':'5','08':'1','09':'4','1':'6','2':'2','3':'2','4':'5',
               '5':'0','6':'3','7':'5','8':'1','9':'4','10':'6',
               '11':'2','12':'4','010':'5','020':'1'})
monthdict2=({'01':'January','02':'February','03':'March','04':'April',
             '05':'May','06':'June','07':'July','08':'August','09':'September'
             ,'1':'January','2':'February','3':'March','4':'April',
             '5':'May','6':'June','7':'July','8':'August','9':'September'
             ,'10':'October','11':'November','12':'December'})
daydict=({'1':'Monday','2':'Tuesday','3':'Wednesday','4':'Thursday',
               '5':'Friday','6':'Saturday','0':'Sunday'})
#Get input and test ranges of allowable input 
while True:
    day=input('Please input the number of the day: ')
    while True:
        if day:
            if day.isdigit():
                if int(day)<=31 and int(day)>=1:
                    break
                else:
                    day=(input('Please input a number between 1-31: ' 
                        ))
        else:
            day=input('Please input the number of the day: ')         
    month=input('Please input the number of the month: ')
    while True:
        if month:
            if month.isdigit():
                if int(month)<=12 and int(month)>=1:
                    break
                else:
                    month=(input('Please input a correct month number 1-12'
                        ': '))
        else:
            month=input('Please input a month: ')
    
    year=input('Please input a year between 1600 and 2799: ')
    while True:
        if year:
            if year.isdigit():
                if int(year)<=2799 and int(year)>=1600:
                    break
                else:
                    year=input('Please input a year between 1600 and 2799:'
                               ' ')
        else:
            year=input('Please input a year: ')
            
    
    
    yearcode=str(year)[-2:]
    centurycode=str(year)[:2]
#Transform year to known year number code 
    while True:
        if int(yearcode)<=27:
            yearfinal=int(yeardict[yearcode])
            break
        elif int(yearcode)>27 and int(yearcode)<=55 :             
            yearcode=str(int(yearcode)-28)
            yearfinal=int(yeardict[yearcode])
            break
        elif int(yearcode)>55 and int(yearcode)<=83:
            yearcode=str(int(yearcode)-56)
            yearfinal=int(yeardict[yearcode])
            break
        elif int(yearcode)>83 and int(yearcode)<=99:
            yearcode=str(int(yearcode)-84)
            yearfinal=int(yeardict[yearcode])
            break
# Account for Leap years
    if int(yearcode)%4==0:
        if int(month)<=2:
            monthfinal=int(monthdict[month])-1
        else:
            monthfinal=int(monthdict[month])
    else:
        monthfinal=int(monthdict[month])
# Find day of week
    daycalc=(monthfinal+yearfinal+int(day)+int(centurydict[centurycode]))%7
    print(daycalc)
        
#    print('The date: ',day,'/',month,'/',year,'falls on', 
#           daydict[str(daycalc)],'.')
    print(monthdict2[str(month)], day+',', year, 'is on a',daydict[str(daycalc)]
        +'.')
    
   # Continue code until terminated by user
    print('Would you like to continue? Type n and press Enter to stop')
    yesno=input()
    if yesno=='n':
        break