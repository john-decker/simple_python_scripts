# randomly_generated_data.py
# python script to generate random numbers and do basic analysis on them
# the maximum number generated should be 100 as the analysis breaks the output into increments of 25

import random 

first_twenty_five = []
second_twenty_five = []
third_twenty_five = []
fourth_twenty_five = []
random_numbers_list = []

# eventually make target_number user input
# could be any number but 100 seems to be best for getting readable output on the simple bar chart
target_number = 100
for i in range(0,target_number):
	new_num = random.randint(1,100)
	random_numbers_list.append(new_num)

#output initial data
print("List of", target_number, "randomly generated numbers from 1 to 100")
print(random_numbers_list)
print()

for number in random_numbers_list:
	if number <=25:
		first_twenty_five.append(number)
	elif number <=50:
		second_twenty_five.append(number)
	elif number <=75:
		third_twenty_five.append(number)
	else:
		fourth_twenty_five.append(number)

print("(Simple Bar Chart)\r")

print("Distribution of 50 randomly generated numbers by ranges:")
print("  0-25:", sorted(first_twenty_five))
print(" 26-50:", sorted(second_twenty_five))
print(" 51-75:", sorted(third_twenty_five))
print("76-100:", sorted(fourth_twenty_five))

print()

# provide % of numbers within 25 point "buckets"
q1 = round((len(first_twenty_five)/target_number)*100)
q2 = round((len(second_twenty_five)/target_number)*100)
q3 = round((len(third_twenty_five)/target_number)*100)
q4 = round((len(fourth_twenty_five)/target_number)*100)

print("Distribution of 50 randomly generated numbers by percentage per quarter")
print("  0-25:", q1, "%")
print(" 26-50:", q2, "%")
print(" 51-75:", q3, "%")
print("76-100:", q4, "%")

print()

# provide the lowest number in each list by using the min function
print("Min number in each quarter")
print("  0-25: lowest =", min(first_twenty_five))
print(" 26-50: lowest =", min(second_twenty_five))
print(" 51-75: lowest =", min(third_twenty_five))
print("76-100: lowest =", min(fourth_twenty_five))

print()

# provide the largest number in each list by using the max function
print("Max number in each quarter")
print("  0-25: highest =", max(first_twenty_five))
print(" 26-50: highest =", max(second_twenty_five))
print(" 51-75: highest =", max(third_twenty_five))
print("76-100: highest =", max(fourth_twenty_five))

print()

# povide average of each list. Sum all the elements and divide by the number of elements in the list
print("Average of all numbers in quarter")
print("  0-25: average ~", round(sum(first_twenty_five)/len(first_twenty_five)))
print(" 26-50: average ~", round(sum(second_twenty_five)/len(second_twenty_five)))
print(" 51-75: average ~", round(sum(third_twenty_five)/len(third_twenty_five)))
print("76-100: average ~", round(sum(fourth_twenty_five)/len(fourth_twenty_five)))

# eventually output to JSON in append mode so that multiple trials can be run and further analysed
print()

# create dictionary titled trial_ditionary use above sections as keys
#filename =  trial_dictionary
#with open(filename, a) as f_obj:
	#JSON.dump(f_obj)
