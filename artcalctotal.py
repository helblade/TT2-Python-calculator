##To use this, you are going to put this script in the file where Python saves
##your scripts. when the shell starts up you are going to type
##import artcalctotal
##x = artcalctotal.start
## after you type those two things all you have to do is type
##x()
##for the script to run, and thats all you have to type until you close or
##restart the shell


def start():
	y = 0
	totalCost = 0
	costBD = []
	printer = 0
	while(y == 0):
		artcat = ['1. Mana reduction','2. Book of Shadows', '3. Heavenly Sword', '4. Damage','5. Gold','6. Skill Mod', '7. Equipment Modifiers']
		print (artcat)
		x = int(input('Which category do you want to calculate?'))
		a = x-1
		a = artcat[a]
		costBD.append(a)
		part = catpick(x)
		totalCost = totalCost + part
		costBD.append(part)
		printer = printer + 2
		z = int(input('Are you finsished?  1. Yes 2. No '))
		if (z == 1):
                        i = 0
                        while(i < printer):
                                
                                print(costBD.pop(0),':',costBD.pop(0))
                                printer = printer - 2
                        print('Your total relic cost is: ', totalCost)
                        return
		else:
			y = 0
##Category Picker
def catpick(x):
	level= int(input('What level is your artifact? '))
	goal= int(input('What is your goal level? '))
	if(x == 1):
		return(manacost(level, goal))
	elif(x == 2):
		return(bos(level, goal))
	elif(x == 3):
		return(hsbop(level, goal))
	elif(x == 4):
		damage = ['1. CotA, BoD, FoE, SoS', '2. DR', '3. Furies']
		print(damage)
		x = int(input('Which artifact are you calculting?'))
		return(dmgsort(x, level,  goal))
	elif(x == 5):
                gold = ['1. Heroic Shield or SoV', '2. BoP', '3. Chest']
                print(gold)
                x = int(input('Which artifact are you calculating? '))
                return(goldsort(x, level, goal))
	elif(x == 6):
		return(skillmod(level,goal))
	elif(x == 7):
                return(eqm(level, goal))

##Sorters

def dmgsort(x, level, goal):
        if(x == 1):
                return(herodmg(level, goal))
        elif(x == 2):
                return(divret(level, goal))
        elif(x == 3):
                return(furies(level, goal))
        else:
                print('error')
                return

def goldsort(x, level, goal):
        if ( x == 1):
                return(mongold(level, goal))
        elif(x == 2):
                return(hsbop(level, goal))
        elif(x == 3):
                return(chest(level, goal))
        else:
                print("error")

##Calcs

def bos(x,y):
        cost = 0
        while (x < y+1):
                exponent = pow(x, 2.5)
                relics = .7 * exponent
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def manacost (x,y):
        cost = 0
        while(x < y+1):
                exponent = pow(x, 3)
                relics = .6*exponent
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def skillmod(x, y):
        cost = 0
        while (x < y+1):
                exponent = pow(x, 1.7)
                relics = .6*exponent
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def herodmg(x, y):
        cost = 0
        while(x < y+1):
                exponent = pow(x, 1.7)
                relics = .7*exponent
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def divret(x, y):
        cost = 0
        while (x < y+1):
                relics = pow(x, 2)
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def hsbop(x, y):
        cost = 0
        while (x < y+1):
                relics = .7*pow(x, 2.2)
                cost = cost + relics
                x = x + 1
                if (x == y):
                        return(cost)

def mongold(x, y):
        cost = 0
        while (x < y+1):
                relics = .7*pow(x, 1.8)
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def chest(x, y):
        cost = 0
        while(x < y+1):
                relics = pow(x, 1.8)
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)

def eqm(x, y):
        cost = 0
        while(x < y+1):
                relics = .65*pow(x, 2)
                cost = cost + relics
                x = x+1
                if(x == y):
                        return(cost)
                
                

def furies(x, y):
        cost = 0
        while (x < y+1):
                relics = .7*pow(x, 2)
                cost = cost + relics
                x = x+1
                if (x == y):
                        return(cost)






        


			
