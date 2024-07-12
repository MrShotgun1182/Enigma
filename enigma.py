import click
from os import system

alphabet = "abcdefghijklmnopqrstuvwxyz "

gearNumber1 = "sxwvjp yqkebntazdoclufhrmig"
gearNumber2 = "c azgmsxwfyrplqduvtbjhnkieo"
gearNumber3 = "lptyoaufwqerhbcsvn jxikzdgm"
gearNumber4 = "qkwjtn sovgizbryecfxdaplmuh"
gearNumber5 = "zemdgirnswlfqubcoxvkath ypj"

answer = ""
counter = 0

def reflector(character):
    index = len(alphabet) - alphabet.find(character) - 1
    return alphabet[index]

def gears(char):
    index1 = alphabet.find(char)
    char1 = gear1[index1]

    index2 = alphabet.find(char1)
    char2 = gear2[index2]

    index3 = alphabet.find(char2)
    char3 = gear3[index3]

    ref = reflector(char3)

    index3 = gear3.find(ref)  # jaiegah peida kon
    char3 = alphabet[index3]  # harf saz

    index2 = gear2.find(char3)
    char2 = alphabet[index2]

    index1 = gear1.find(char2)
    char1 = alphabet[index1]

    return char1

def shift ():
    global counter, gear1, gear2, gear3
    gear1 = gear1[1:] + gear1[0]
    counter += 1 

    if counter % 27 == 0 :
        gear2 = gear2[1:] + gear2[0]
    
    if counter % (27 * 27) == 0 :
        gear3 = gear3[1:] + gear3[0]

def getGear(inputGear):
    if inputGear == 1:
        return gearNumber1
    
    if inputGear == 2:
        return gearNumber2
    
    if inputGear == 3:
        return gearNumber3
    
    if inputGear == 4:
        return gearNumber4 
    
    if inputGear == 5: 
        return gearNumber5    
        
inputGear1 = int(input ("shomare charkhdande 1 ra vared konid: "))
gear1 = getGear(inputGear1)

inputGear2 = int(input ("shomare charkhdande 2 ra vared konid: "))
gear2 = getGear(inputGear2)

inputGear3 = int(input ("shomare charkhdande 3 ra vared konid: "))
gear3 = getGear(inputGear3)

inputCahr = ''
print('Enter your text: ', end='')

while inputCahr != '!':
    system('cls')
    print(answer)
    inputCahr = click.getchar()
    answer += gears(inputCahr)
    shift ()

print('its don!!!')
