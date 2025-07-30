'''
    author: Mohit Singh
    date: 31/07/2025
    version: 1
    description: writing a program that asks for and stores the users height and age.
'''
#------libary-----------------
import random
#------functions--------------



#-----main routine------------
#My way
#print('Dreamworld - are you eligible to take the rides')
#height = int(input('what is your height in cm?: '))
#if (height > 150):
    #print('You are eligible for Stratosfear, Family Karts, Scorpion Karts')
#if (height >120):
    #print('You are eligible for Fearfall, Invader, Corkscrew Roller Coaster, Bumber boat')
#age = int(input('What is your age'))
#if (height <= 90 and height <= 120 and age <= 5):
    #print('You are eligible to go onto the Log Flume, Gold Rush, Family Karts(passenger only), Dogems (passenger only)')
#if (height >=80 and age <=2 and age >=9):
    #print('You can go in the fortess of fun')

#Teachers way
print('Dreamworld - are you eligible to take the rides')
height = float(input('Enter your height: ')) #float or decimal
age = int(input('Enter your age: ')) #turning to number integ

if(height >150):
    print('Stratosfear, Family Karts, Scorpion Karts')
if(height >120):
    print('Fearfall, Invader, Corkscrew Roller Coaster, Bumber boat')
if(height > 90 and age >5):
    print('Los Banditos')
    if(age > 8):
        print('Robot Riot')
if(height >80):
    print('Log Flume, Gold Rush, Family Karts, Dogems')
elif(height < 80 and age >=3 and age <=8):
    print('fortess of fun')
