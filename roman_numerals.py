# roman_numerals.py
# python script to convert Arabic numbers to Roman numerals

# eventually make this user input
number = 1999

#initialize variables for year places
thousands = 0
five_hundreds = 0
hunreds = 0
fifties = 0
tens = 0
fives = 0
ones = 0

#break input into year chuncks
thousands = number//1000
five_hundreds = (number-(thousands*1000))//500
hundreds = (number-(thousands*1000)-(five_hundreds*500))//100
fifties = (number-(thousands*1000)-(five_hundreds*500)-(hundreds*100))//50
tens = (number-(thousands*1000)-(five_hundreds*500)-(hundreds*100)-(fifties*50))//10
fives = (number-(thousands*1000)-(five_hundreds*500)-(hundreds*100)-(fifties*50)-(tens*10))//5
ones = (number-(thousands*1000)-(five_hundreds*500)-(hundreds*100)-(fifties*50)-(tens*10)-(fives*5))//1

# set for output by numeral
m = "M"*thousands
d = "D"*five_hundreds
c = "C"*hundreds
l = "L"*fifties
x = "X"*tens
v = "V"*fives
i = "I"*ones

# test for special cases
# output 900 as CM
if (five_hundreds*500)+(hundreds*100) == 900:
	d = ""
	c = "CM"

#output 90 as XC	
if (fifties*50)+(tens*10) == 90:
	l = "XC"
	x = ""

#output 9 as IX	
if (fives*5)+(ones*1) == 9:
	v = ""
	i = "IX"

#output 4 as IV
if (fives*5)+(ones*1) == 4:
	i = "IV"
	

print(number, "=", m+d+c+l+x+v+i)
