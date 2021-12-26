lastdigit = "even" if int(input("What is the last digit of the serial number? ")) % 2 == 0 else "odd"
serialvowel = True if int(input("Does the serial code have a vowel in it? (0/1) ")) == 1 else False
batteries = int(input("How many batteries? "))

def wires():
	numwires = int(input("How many wires are there? "))
	lastwire = str(input("What is the colour of the last wire? "))
	lastwire = lastwire.lower()
	redwires = int(input("How many red wires are there? "))
	bluewires = int(input("How many blue wires are there? "))

	# print(f"There are {str(numwires)} wires, the last wire is {lastwire}, there are {str(redwires)} red wires and {str(bluewires)} blue wires.")

	if numwires == 3:
		if redwires == 0:
			return "Cut the second wire"
		else:
			if lastwire == "white":
				return "Cut the last wire"
			else:
				if bluewires > 1:
					return "Cut the last blue wire"
				else:
					return "Cut the last wire"

	if numwires == 4:
		if redwires > 1 and lastdigit == "odd":
			return "Cut the last red wire"
		else:
			if (lastwire == "yellow" and redwires == 0) or bluewires == 1:
				return "Cut the first wire"
			else:
				yellowwires = int(input("How many yellow wires are there? "))
				if yellowwires > 1:
					return "Cut the last wire"
				else:
					return "Cut the second wire"

	if numwires == 5:
		if lastwire == "black" and lastdigit == "odd":
			return "Cut the fourth wire"
		else:
			yellowwires = int(input("How many yellow wires are there? "))
			if redwires == 1 and yellowwires > 1:
				return "Cut the first wire"
			else:
				blackwires = int(input("How many black wires are there? "))
				if blackwires == 0:
					return "Cut the second wire"
				else:
					return "Cut the first wire"

	if numwires == 6:
		yellowwires = int(input("How many yellow wires are there? "))
		if yellowwires == 0 and lastdigit == "odd":
			return "Cut the third wire"
		else:
			whitewires = int(input("How many white wires are there? "))
			if yellowwires == 1 and whitewires > 1:
				return "Cut the fourth wire"
			else:
				if redwires == 0:
					return "Cut the last wire"
				else:
					return "Cut the fourth wire"
	
	return "Error, try again"

def button():
	btnred = int(input("Is the button red? (0/1) "))
	btnhold = int(input("Does the button say 'Hold' (0/1)? "))
	btndet = int(input("Does the button say 'Detonate' (0/1)? "))
	

	if batteries > 1 and btndet == 1:
		return "Press and immediately release"
		
	frk = int(input("Is there a lit indicator FRK? (0/1) "))

	if batteries > 2 and frk == 1:
		return "Press and immediately release"

	if btnred == 1 and btnhold == 1:
		return "Press and immediately release"

	print("Hold the button.")

	# Holding	
	holdcolour = input("What colour is the strip? ")
	holdcolour = holdcolour.lower()

	if holdcolour == "blue":
		return "Release when the timer has a 4"
	elif holdcolour == "yellow":
		return "Release when the timer has a 5"
	else:
		return "Release when the timer has a 1"

def keypad():
	print("Enter your symbol names seperated by a space: ")
	symbols = input().split()

	columns = [["head","triforce","lambda","lightning","alien","H","backc"],["backe","head","backc","e","stare","H","?"],["copyright","w","e","K","R","lambda","stare"],["6","P","b","alien","K","?","face"],["trident","face","b","c","P","3","starf"],["6","backe","puzzle","ae","trident","N","omega"]]

	answer = []
	tocheck = 0
	while len(answer) < 4:
		if tocheck >= len(columns):
			return "Error: could not solve that sequence"
		
		answer = []

		for i in range(len(columns[tocheck])):
			for j in range(len(symbols)):
				if symbols[j] == columns[tocheck][i]:
					answer.append(symbols[j])

		tocheck += 1
	
	return " ".join(answer)

def simon():
	strikes = int(input("How many strikes do you have? "))

	while True:
		print("Enter the colours (in letters) or 'e' to exit module: ")
		cols = input().lower().split("")
		if cols[0] == "e":
			return "Module finished"
		ans = []

		for k in range(len(cols)):
			if serialvowel:
				if strikes == 0:
					if cols[k] == "r": ans.append("Blue")
					if cols[k] == "b": ans.append("Red")
					if cols[k] == "g": ans.append("Yellow")
					if cols[k] == "y": ans.append("Green")
				elif strikes == 1:
					if cols[k] == "r": ans.append("Yellow")
					if cols[k] == "b": ans.append("Green")
					if cols[k] == "g": ans.append("Blue")
					if cols[k] == "y": ans.append("Red")
				else:
					if cols[k] == "r": ans.append("Green")
					if cols[k] == "b": ans.append("Red")
					if cols[k] == "g": ans.append("Yellow")
					if cols[k] == "y": ans.append("Blue")
			else:
				if strikes == 0:
					if cols[k] == "r": ans.append("Blue")
					if cols[k] == "b": ans.append("Yellow")
					if cols[k] == "g": ans.append("Green")
					if cols[k] == "y": ans.append("Red")
				elif strikes == 1:
					if cols[k] == "r": ans.append("Red")
					if cols[k] == "b": ans.append("Blue")
					if cols[k] == "g": ans.append("Yellow")
					if cols[k] == "y": ans.append("Green")
				else:
					if cols[k] == "r": ans.append("Yellow")
					if cols[k] == "b": ans.append("Green")
					if cols[k] == "g": ans.append("Blue")
					if cols[k] == "y": ans.append("Red")
		
		return(" ".join(ans))

def wof():
	for q in range(5):

		# input display
		disp = input("What does the display say? (enter 'b' for empty display)").lower()
		
		# find and output location for that word(s)
		if disp == "ur":
			pos = "top left"
		elif disp == ("first" or "okay" or "c"):
			pos = "top right"
		elif disp == ("yes" or "nothing" or "led" or "they are"):
			pos = "middle left"
		elif disp == ("b" or "reed" or "leed" or "they're"):
			pos = "bottom left"
		elif disp == ("blank" or "read" or "red" or "you" or "your" or "you're" or "their"):
			pos = "middle right"
		else:
			pos = "bottom right"

		# input that location's label
		label = input(f"What is the label at position {pos.upper()}? ")
		label = label.lower()

		# output all words until label is repeated and then go to the next stage
		wordsdict = {
			'ready':'yes, okay, what, middle, left, press, right, blank, ready', 'first':'left, okay, yes, middle, no, right, nothing, uhhh, wait, ready, blank, what, press, first', 'no':'blank, uhhh, wait, first, what, ready, right, yes, nothing, left, press, okay, no', 'blank':'wait, right, okay, middle, blank', 'nothing':'uhhh, right, okay, middle, yes, blank, no, press, left, what, wait, first, nothing', 'yes':'okay, right, uhhh, middle, first, what, press, ready, nothing, yes', 'what':'uhhh, what', 'uhhh':'ready, nothing, left, what, okay, yes, right, no, press, blank, uhhh', 'left':'right, left', 'right':'yes, nothing, ready, press, no, wait, what, right', 'middle':'blank, ready, okay, what, nothing, press, no, wait, left, middle', 'okay':'middle, no, first, yes, uhhh, nothing, wait, okay', 'wait':'uhhh, no, blank, okay, yes, left, first, press, what, wait', 'press':'right, middle, yes, ready, press', 'you':'sure, you are, your, you\'re, next, uh huh, ur, hold, what?, you', 'you are':'your, next, like, uh huh, what?, done, uh uh, hold, you, u, you\'re, sure, ur, you are', 'your':'uh uh, you are, uh huh, your', 'you\'re':'you, you\'re', 'ur':'done, u, ur', 'u':'uh huh, sure, next, what?, you\'re, ur, uh uh, done, u', 'uh huh':'uh huh', 'uh uh':'ur, u, you are, you\'re, next, uh uh', 'what?':'you, hold, you\'re, your, u, done, uh uh, like, you are, uh huh, ur, next, what?', 'done':'sure, uh huh, next, what?, your, ur, you\'re, hold, like, you, u, you are, uh uh, done', 'next':'what?, uh huh, uh uh, your, hold, sure, next', 'hold': 'you are, u, done, uh uh, you, ur, sure, what?, you\'re, next, hold', 'sure':'you are, done, like, you\'re, you, hold, uh huh, ur, sure', 'like':'you\'re, next, u, ur, hold, done, uh uh, what?, uh huh, you, like'
		}
		print(wordsdict[str(label)])
	return "Module finished"

def memory():
	# using i to count stages
	i = 1

	while True:
		# input display
		disp = input("What does the display say? (press 'e' to exit module) ")
		if disp == "e":
			return "Module cancelled"
		disp == int(disp)

		# find and output instruction and record position & label for each in an array [pos,lab]
		if i == 1:
			if disp == 1 or disp == 2:
				print("Press the button in position 2")
				lab = input("What label is that? ")
				stage1 = ['2',lab]
				i += 1
			elif disp == 3:
				print("Press the button in position 3")
				lab = input("What label is that? ")
				stage1 = ['3',lab]
				i += 1
			elif disp == 4:
				print("Press the button in position 4")
				lab = input("What label is that? ")
				stage1 = ['4',lab]
				i += 1

		elif i == 2:
			if disp == 1:
				print("Press the button with label 4")
				pos = input("What position is that?")
				stage2 = [pos,'4']
				i += 1
			elif disp == 3:
				print("Press the button in position 1")
				lab = input("What label is that? ")
				stage2 = ['1',lab]
				i += 1
			elif disp == 2 or disp == 4:
				print(f"Press the button in position {stage1[0]}")
				lab = input("What label is that?")
				stage2 = [stage1[0],lab]
				i += 1

		elif i == 3:
			if disp == 1:
				print(f"Press the button with label {stage2[1]}")
				pos = input("What position is that? ")
				stage3 = [pos,stage2[1]]
				i += 1
			elif disp == 2:
				print(f"Press the button with label {stage1[1]}")
				pos = input("What position is that? ")
				stage3 = [pos,stage1[1]]
				i += 1
			elif disp == 3:
				print("Press the button in position 3")
				lab = input("What label is that? ")
				stage3 = ['3',lab]
				i += 1
			elif disp == 4:
				print("Press the button with label 4")
				pos = input("What position is that?")
				stage3 = [pos,'4']
				i += 1

		elif i == 4:
			if disp == 1:
				print(f"Press the button in position {stage1[0]}")
				lab = input("What label is that? ")
				stage4 = [stage1[0],lab]
				i += 1
			elif disp == 2:
				print("Press the button in position 1")
				lab = input("What label is that? ")
				stage4 = ['1',lab]
				i += 1
			elif disp == 3 or disp == 4:
				print("Press the button in position 2")
				lab = input("What label is that? ")
				stage4 = ['2',lab]
				i += 1

		elif i == 5:
			if disp == 1:
				return f"Press the button with label {stage1[1]}"
			elif disp == 2:
				return f"Press the button with label {stage2[1]}"
			elif disp == 3:
				return f"Press the button with label {stage4[1]}"			
			elif disp == 4:
				return f"Press the button with label {stage3[1]}"

def morse():

	morsecodedict = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..'}

	print("Input the message in dots(.) and dashes(-) with each letter seperated by a space: ")
	message = input()

	message += ' '
	decipher = ''
	citext = ''
	for letter in message:
		if (letter != ' '):
			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :
				decipher += ' '
			else:
				decipher += list(morsecodedict.keys())[list(morsecodedict.values()).index(citext)]
				citext = ''
	
	return decipher

def compwires():
	parallel = True if int(input("Is there a parallel port? (0/1) ")) == 1 else False
	while True:
		exit = input("Enter 'e' to exit, or just press enter to continue ")
		if exit == 'e':
			return "Module finished/cancelled"
		
		star = True if int(input("Is there a star? (0/1) ")) == 1 else False
		led = True if int(input("Is the led lit? (0/1) ")) == 1 else False
		white = True if int(input("Is the wire just white? (0/1) ")) == 1 else False

		if white:
			if star and led:
				print("Cut") if batteries > 2 else print("Don't cut")
			elif led:
				print("Don't cut")
			else:
				print("Cut")
		else:
			red = True if int(input("Is there red? (0/1) ")) == 1 else False
			blue = True if int(input("Is there blue? (0/1) ")) == 1 else False

			if (not star) and (not led):
				print("Cut") if lastdigit == "even" else print("Don't cut")
			else:
				if red and blue: # red + blue
					if star and led:
						print("Don't cut")
					elif star:
						print("Cut") if parallel else print("Don't cut")
					elif led:
						print("Cut") if lastdigit == "even" else print("Don't cut")
				
				elif red: # just red / red + white (same)
					if star and (not led):
						print("Cut")
					else:
						print("Cut") if batteries > 2 else print("Don't cut")
				
				else: # just blue / blue + white (same)
					if star and (not led):
						print("Don't cut")
					else:
						print("Cut") if parallel else print("Don't cut")

def wireseqs():
	reds = 0
	blues = 0
	blacks = 0
	while True:
		foundcolour = False		
		while not foundcolour:

			# input color and letter the wire's connected to into an array [col,let]
			wire = input("Enter the color and letter seperated by a space or 'e' to stop: ").lower().split()			
			if wire[0] == 'e':
				reds = 0
				blues = 0
				blacks = 0
				return "Module finished/cancelled"
			
			# increment the counter for that colour
			# then check with the manual for if to cut (first will be {var} 1)

			if wire[0] == "red":
				foundcolour = True
				reds += 1

				foundletter = False
				while not foundletter: 
					if wire[1] == 'a':
						foundletter = True
						if reds == 3 or reds == 4 or reds == 6 or reds == 7 or reds == 8:
							print("Cut")
						else:
							print("Don't cut")

					elif wire[1] == 'b':
						foundletter = True
						if reds == 2 or reds == 5 or reds == 7 or reds == 8 or reds == 9:
							print("Cut")
						else:
							print("Don't cut")
					
					elif wire[1] == 'c':
						foundletter = True
						if reds == 1 or reds == 4 or reds == 6 or reds == 7:
							print("Cut")
						else:
							print("Don't cut")

			elif wire[0] == "blue":
				foundcolour = True
				blues += 1

				foundletter = False
				while not foundletter: 
					if wire[1] == 'a':
						foundletter = True
						if blues == 2 or blues == 4 or blues == 8 or blues == 9:
							print("Cut") 
						else:
							print("Don't cut")

					elif wire[1] == 'b':
						foundletter = True
						if blues == 1 or blues == 3 or blues == 5 or blues == 6:
							print("Cut")
						else:
							print("Don't cut")
					
					elif wire[1] == 'c':
						foundletter = True
						if blues == 2 or blues == 6 or blues == 7 or blues == 8:
							print("Cut")
						else:
							print("Don't cut")

			elif wire[0] == "black":
				foundcolour = True
				blacks += 1

				foundletter = False
				while not foundletter: 
					if wire[1] == 'a':
						foundletter = True
						if blacks == blacks == 1 or blacks == 2 or blacks == 4 or blacks == 7:
							print("Cut") 
						else:
							print("Don't cut")

					elif wire[1] == 'b':
						foundletter = True
						if blacks == blacks == 1 or blacks == 3 or blacks == 5 or blacks == 6 or blacks == 7:
							print("Cut")
						else:
							print("Don't cut")
					
					elif wire[1] == 'c':
						foundletter = True
						if blacks == 1 or blacks == 2 or blacks == 4 or blacks == 6 or blacks == 8 or blacks == 9:
							print("Cut")
						else:
							print("Don't cut")

# Game loop
while True:
	module = input("Enter module or 'e' to stop: ")
	module = module.lower()
	if module == "e":
		print("\nIf you defused it, well done!\n\n..if you didn't, gl for next time lol")
		break
	if module == "wire" or module == "wires":
		print(wires())
	elif module == "button" or module == "buttons":
		print(button())
	elif module == "keypad" or module == "keypads":
		print(keypad())
	elif module == "simon" or module == "simon says":
		print(simon())
	elif module == ("wof" or "wof?" or "whos on first" or "who's on first" or "whos on first?" or "who's on first?"):
		print(wof())
	elif module == "memory" or module == "mem":
		print(memory())
	elif module == "morse" or module == "morse code":
		print(morse())
	elif module == "complicated wires" or module == "complicated" or module == "comp wires" or module == "comp":
		print(compwires())
	elif module == "wire sequences" or module == "wire sequence" or module == "wire seq" or module == "seq" or module == "wire seqs" or module == "seqs" or module == "sequence" or module == "sequences":
		print(wireseqs())

	else:
		print("Module not found")