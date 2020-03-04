# python script to convert standard English to Pig Latin


# converts individual word
def to_pig_latin(start_word):
	first_letter = start_word[0]
	remaining_word = start_word[1:]
	# removes period from the end of a word
	if remaining_word[-1] == ".":
		remaining_word = remaining_word[:-1]

	suffix = 'ay'
	pig_latin = remaining_word+first_letter+suffix

	# preserves capitalization -- if word was capitalized in original, new word will be capitalized
	if first_letter.isupper():
		pig_latin = pig_latin.lower()
		pig_latin = pig_latin.title()
	else:
		pig_latin = pig_latin.lower()
	return pig_latin

# converts sentence  
def sentence_to_pig_latin(sentence):
	new_sentence = []
	counter = 0
	for word in sentence:
		word = to_pig_latin(word)
		new_sentence.append(word)
		counter += 1
	new_sentence = convert_to_string(new_sentence, " ")
	return new_sentence

# rejoins list of individual words to sentence
def convert_to_string(input_list, separator):
	final_string = separator.join(input_list)
	return final_string

# test strings -- eventually rework to make user input
test_sentence = "Hello and welcome to the course on Pig Latin"
test_sentence2 = "The quick brown fox"
test_sentence3 = "Robin went to the Sheriff of Nottingham to plead on behalf of the people of the forest."
# test_sentence3 = "The quickest way to Saint George is through Martinville"

# breaks sentences into lists of individual words
# eventually make into function to hanlde use input
sentence_list = test_sentence.split()
sentence_list2 = test_sentence2.split()
sentence_list3 = test_sentence3.split()

# output results
# final punctuation must be added because it is stripped in the conversion process
print(test_sentence + ":\r")
print(sentence_to_pig_latin(sentence_list) + ". \n")

print(test_sentence2 + ":\r")
print(sentence_to_pig_latin(sentence_list2) + ". \n")

print(test_sentence3 + ":\r")
print(sentence_to_pig_latin(sentence_list3) + ". \n")
