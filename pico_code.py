from machine import ADC
from time import sleep

totalAmph=60
adcpin = 26
pinToRead = ADC(adcpin)
sumNumber=0
current=0
counter = 0
sumCurrent = 0
avgCurrent = 0
width = 0.1
percentage = 0
conversionConstant = 1

# 3.02 amps (1440)

while True:
    current = pinToRead.read_u16() * conversionConstant
    counter += 1
    sumCurrent += current
   
    avgCurrent = sumCurrent / counter
   
    area=width*current
    sumNumber=sumNumber+area
    percentage=(totalAmph-sumNumber)/totalAmph
    sleep(0.1)
   
    print(percentage)

