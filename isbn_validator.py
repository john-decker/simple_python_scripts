# short python script to check validity of ISBN 10
# not meant to validate isbns other than ISBN 10

def isbn_validator(isbn):
	running_total=0
	multiplier=10
	for char in isbn:
		if char == "X":
			char = "10"
			val=int(char)
		else:
			val=int(char) 
		new=val*multiplier
		running_total += new
		multiplier -= 1
	is_valid = running_total%11
	if is_valid == 0:
		return True
	else:
		return False

def validator_output(isbn):
	if isbn_validator(isbn) == True:
		message = "ISBN " + isbn + " is valid."
	else:
		message = "ISBN " + isbn + " is NOT valid."
	return message

# eventually reconfigure to accept user input with validation 
isbn="0747532699"
isbn2="156881111X"
isbn3="0747532789"

print(validator_output(isbn3))






