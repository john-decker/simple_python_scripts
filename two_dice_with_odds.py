# python script to roll two die randomly, output the number of ways that number can be reached, 
# and give odds of rolling that number

import random

#eventually make the number of sides user input, set minimum sides to 4 and validate
die1 = 8
die2 = 8

# variation -- randomly assigns dice with sides from 4 to 20
# allows for odd-sided die (e.g. 17-sided)
# die1 = random.randint(4,20)
# die2 = random.randint(4,20)

# ensure that rolled number goes no lower than 2 and no higher than the total of the two dice
roll = random.randint(2, (die1 + die2))

combo_counter = 0
combo_breakdown = []

# because each die starts at 1, the die total has to be given one extra to keep the count correct
for i in range(1,die1+1):
	for j in range(1,die2+1):
		new_number = i+j
		if new_number == roll:
			# look for the number if the number is found count it
			combo_counter +=1
			# format and save combinations for later output
			target_combo = str(i) + " + " + str(j) + " = " + str(roll)
			combo_breakdown.append(target_combo)
		else:
			continue

#begin output			
print("You rolled", roll)

# handle various die combinations
if die1 == die2:
	dice_message = "using two " + str(die1) + "-sided dice"
else:
	dice_message = "using a " + str(die1) + "-sided die and a " + str(die2) + "-sided die"

# output number of ways to achieve the roll
if combo_counter == 1:
	print("There is one way to roll ", roll, dice_message)
else:
	print("There are", combo_counter, "ways to roll", roll, dice_message)

for element in combo_breakdown:
	print(element)

# give odds
odds = round(combo_counter/(die1*die2),3)*100

print("The odds of rolling", roll, "are", odds, "%")