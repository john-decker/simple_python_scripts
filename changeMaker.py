#changeMaker.py
#script for calculating bills and coins needed to efficiently make change

# eventually rework to make this user or system input with validation
starting_amount = 36.41 

#initialize main variables
dollar=0
twenty=0
ten=0
five=0
single=0
cent=0
quarter=0
dime=0
nickle=0
penny=0


#increases precision to help offset rounding and ensure proper change
sum_in_cents = round((starting_amount * 100),3) 

#tests to see if amount is negative, which would mean money was still due
if(starting_amount < 0):
	print("Sorry, ", starting_amount, " is invalid. \r")
	starting_amount = 0;

#tests to see if any change is due at all
elif(starting_amount == 0):
	print("No Change Due")

# need to test for whether or not the input is numeric
# may need a try/except looking for ValueError
# currently not working
# elif type(starting_amount) == str:
# 	print("Sorry, ", starting_amount, " must be a number.")
# 	starting_amount = 0;

#calculates change above one dollar
elif(sum_in_cents >= 100):
	#calculate bills needed for change over 5 dollars
	dollar = int(sum_in_cents/100)
	twenty = int(dollar/20)
	ten = int((dollar-(twenty*20))/10)
	five = int((dollar-(twenty*20)-(ten*10))/5)
	single = int((dollar-(twenty*20)-(ten*10)-(five*5))/1)
	#calculate change
	cent = int(sum_in_cents-(dollar*100)) #accounts for totals above one dollar
	quarter = int(cent/25)
	dime = int((cent-(quarter*25))/10)
	nickle = int((cent-(quarter*25)-(dime*10))/5)
	penny = int((cent-(quarter*25)-(dime*10)-(nickle*5))/1)
#calculates change under one dollar
else: 
	cent = int(sum_in_cents)
	quarter = int(cent/25)
	dime = int((cent-(quarter*25))/10)
	nickle = int((cent-(quarter*25)-(dime*10))/5)
	penny = int((cent-(quarter*25)-(dime*10)-(nickle*5))/1)

#count total number of bills and coins needed for change
num_bills=(twenty + ten + five + single)
num_coins=(quarter + dime + nickle + penny)

# handle single or plural endings for currency
# assumes plural and tests for single
twenty_message = "twenties,"
ten_message = "tens,"
five_message = "fives,"
single_message = "ones"
quarter_message = "quarters,"
dime_message = "dimes,"
nickle_message = "nickles,"
penny_message = "pennies"

if twenty == 1:
	twenty_message = "twenty,"

if ten == 1:
	ten_message = "ten,"

if five == 1:
	five_message = "five,"

if single == 1:
	single_message = "one"

if quarter == 1:
	quarter_message = "quarter,"

if dime == 1:
	dime_message = "dime,"

if nickle == 1:
	nickle_message = "nickle,"

if penny == 1:
	penny_message = "penny"

#output needed bills and coins to make change
print("Change Due: ", starting_amount, "\r")
print("Bills (", num_bills, "):\r", twenty, twenty_message, ten, ten_message, five, five_message, single, single_message) 
print("Coins (", num_coins, "):\r", quarter, quarter_message, dime, dime_message, nickle, nickle_message, penny, penny_message)
