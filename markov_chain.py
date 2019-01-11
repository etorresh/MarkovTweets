# -*- coding: utf-8 -*-

# Markov chain customized for Twitter bot.
# Made by MadreNodriza. https://github.com/MadreNodriza 


import random
import string_control

def read_file(filename):
	with open(filename, "r", encoding = "utf-8") as file:
		content = file.read().replace("\n", " ")
	return content
	
def build_chain(source, chain = {}):
	words = source.split(" ")
	index = 1
	for word in words[index:]:
		key = words[index - 1]
		if key in chain:
			chain[key].append(word)
		else:
			chain[key] = [word]
		index += 1
	return chain

def create_message(chain, max = 40, starting_sentence = ""):
	if(starting_sentence != ""):
		starting_sentence = string_control.less_spaces(starting_sentence)
		starting_sentence = starting_sentence.strip()
		starting_sentence = string_control.remove_non_alpha_endings(starting_sentence)
		word1 = starting_sentence.split(" ")[-1]
		message = starting_sentence
		if(word1 not in chain):
			print("Warning: Choosing random starting word.")
			word1 = random.choice(list(chain.keys()))
	else:
		word1 = random.choice(list(chain.keys()))
		message = word1.capitalize()

	while(len(message.split(" ")) < max):
		# Check if word limit is reached and if it's true end while loop.
		if(word1 not in chain):
			print("Warning: Word limit reached.")
			return message
		
		word2 = random.choice(chain[word1])
		word1 = word2
		message += " " + word2
		last_word = message[len(message) - 1]
	
	message = string_control.only_periods(message)
	
	if(str.isalpha(last_word) == False and last_word.isdigit == False):
		print("Warning: Removing nonalpha last character and replacing it with a period.")
		message = message[:-1] + "."
	elif(last_word != "."):
		print("Warning: Adding a period.")
		message = message + "."
	return message