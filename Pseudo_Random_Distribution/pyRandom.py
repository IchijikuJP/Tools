# Classical Usage : Critical Rate in Warcraft Ⅲ
# Python Random Lib  
# print posibility of spacific given number from 0 to 100

import random
sum = 0
times = 10000
any_num = 100 #between 0~100 
for i in range(times) :
    sum += True if round(random.random() *100) == any_num else False 

print(round(sum/times*100 ,2) ,"%") 
# Conclusion : 
# nearly 1.000% among [1,99], 0.500% between 0 and 100