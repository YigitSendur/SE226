num = int(input("give time as second : "))
hours = num // 3600
minute = (num-hours*3600)//60
sec=(num-hours*3600-minute*60)
print(str(num) + " second is " + str(hours) + " hours , "+ str(minute) +"minutes , " + str(sec) + " seconds")