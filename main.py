# constants
lastdigit = "undefined"
batteries = "undefined"
serialvowel = "undefined"
frk = "undefined"


def wires():
    global lastdigit

    if lastdigit == "undefined":
        lastdigit = (
            "even"
            if int(input("What is the last digit of the serial number? ")) % 2 == 0
            else "odd"
        )

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
    global batteries
    global frk

    if batteries == "undefined":
        batteries = int(input("How many batteries? "))

    btnred = int(input("Is the button red? (0/1) "))
    btnhold = int(input("Does the button say 'Hold' (0/1)? "))
    btndet = int(input("Does the button say 'Detonate' (0/1)? "))

    if batteries > 1 and btndet == 1:
        return "Press and immediately release"

    if frk == "undefined":
        frk = int(input("Is there a lit indicator FRK? (0/1) "))

    if batteries > 2 and frk == 1:
        return "Press and immediately release"

    if btnred == 1 and btnhold == 1:
        return "Press and immediately release"

    print("Hold the button.")
    print("Blue strip: Release with a 4")
    print("Yellow strip: Release with a 5")
    print("Other strip: Release with a 1")

    return ""


def keypad():
    print("Enter your symbol names separated by a space: ")
    symbols = input().split()

    columns = [
        ["head", "triforce", "lambda", "lightning", "alien", "H", "backc"],
        ["backe", "head", "backc", "e", "stare", "H", "?"],
        ["copyright", "w", "e", "K", "R", "lambda", "stare"],
        ["6", "P", "b", "alien", "K", "?", "face"],
        ["trident", "face", "b", "c", "P", "3", "starf"],
        ["6", "backe", "puzzle", "ae", "trident", "N", "omega"],
    ]

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
    global serialvowel

    if serialvowel == "undefined":
        serialvowel = (
            True
            if int(input("Does the serial code have a vowel in it? (0/1) ")) == 1
            else False
        )

    strikes = int(input("How many strikes do you have? "))

    while True:
        print("Enter the colours (together in letters) or 'e' to exit module: ")
        cols = list(input().lower())
        if cols[0] == "e":
            return "Module finished"
        ans = []

        for k in range(len(cols)):
            if serialvowel:
                if strikes == 0:
                    if cols[k] == "r":
                        ans.append("Blue")
                    if cols[k] == "b":
                        ans.append("Red")
                    if cols[k] == "g":
                        ans.append("Yellow")
                    if cols[k] == "y":
                        ans.append("Green")
                elif strikes == 1:
                    if cols[k] == "r":
                        ans.append("Yellow")
                    if cols[k] == "b":
                        ans.append("Green")
                    if cols[k] == "g":
                        ans.append("Blue")
                    if cols[k] == "y":
                        ans.append("Red")
                else:
                    if cols[k] == "r":
                        ans.append("Green")
                    if cols[k] == "b":
                        ans.append("Red")
                    if cols[k] == "g":
                        ans.append("Yellow")
                    if cols[k] == "y":
                        ans.append("Blue")
            else:
                if strikes == 0:
                    if cols[k] == "r":
                        ans.append("Blue")
                    if cols[k] == "b":
                        ans.append("Yellow")
                    if cols[k] == "g":
                        ans.append("Green")
                    if cols[k] == "y":
                        ans.append("Red")
                elif strikes == 1:
                    if cols[k] == "r":
                        ans.append("Red")
                    if cols[k] == "b":
                        ans.append("Blue")
                    if cols[k] == "g":
                        ans.append("Yellow")
                    if cols[k] == "y":
                        ans.append("Green")
                else:
                    if cols[k] == "r":
                        ans.append("Yellow")
                    if cols[k] == "b":
                        ans.append("Green")
                    if cols[k] == "g":
                        ans.append("Blue")
                    if cols[k] == "y":
                        ans.append("Red")

        print(" ".join(ans))


def wof():
    for q in range(5):
        # input display
        disp = input(
            "What does the display say? (enter 'b' for empty display or 'e' to exit) "
        ).lower()

        if disp == "e":
            return "Module cancelled/finished"

        # find and output location for that word(s)
        if disp == "ur":
            pos = "top left"
        elif disp == "first" or disp == "okay" or disp == "c":
            pos = "top right"
        elif disp == "yes" or disp == "nothing" or disp == "led" or disp == "they are":
            pos = "middle left"
        elif disp == "b" or disp == "reed" or disp == "leed" or disp == "they're":
            pos = "bottom left"
        elif (
            disp == "blank"
            or disp == "read"
            or disp == "red"
            or disp == "you"
            or disp == "your"
            or disp == "you're"
            or disp == "their"
        ):
            pos = "middle right"
        else:
            pos = "bottom right"

        # input that location's label
        label = input(f"What is the label at position {pos.upper()}? ")
        label = label.lower()

        # output all words until label is repeated and then go to the next stage
        wordsdict = {
            "ready": "yes, okay, what, middle, left, press, right, blank, ready",
            "first": "left, okay, yes, middle, no, right, nothing, uhhh, wait, ready, blank, what, press, first",
            "no": "blank, uhhh, wait, first, what, ready, right, yes, nothing, left, press, okay, no",
            "blank": "wait, right, okay, middle, blank",
            "nothing": "uhhh, right, okay, middle, yes, blank, no, press, left, what, wait, first, nothing",
            "yes": "okay, right, uhhh, middle, first, what, press, ready, nothing, yes",
            "what": "uhhh, what",
            "uhhh": "ready, nothing, left, what, okay, yes, right, no, press, blank, uhhh",
            "left": "right, left",
            "right": "yes, nothing, ready, press, no, wait, what, right",
            "middle": "blank, ready, okay, what, nothing, press, no, wait, left, middle",
            "okay": "middle, no, first, yes, uhhh, nothing, wait, okay",
            "wait": "uhhh, no, blank, okay, yes, left, first, press, what, wait",
            "press": "right, middle, yes, ready, press",
            "you": "sure, you are, your, you're, next, uh huh, ur, hold, what?, you",
            "you are": "your, next, like, uh huh, what?, done, uh uh, hold, you, u, you're, sure, ur, you are",
            "your": "uh uh, you are, uh huh, your",
            "you're": "you, you're",
            "ur": "done, u, ur",
            "u": "uh huh, sure, next, what?, you're, ur, uh uh, done, u",
            "uh huh": "uh huh",
            "uh uh": "ur, u, you are, you're, next, uh uh",
            "what?": "you, hold, you're, your, u, done, uh uh, like, you are, uh huh, ur, next, what?",
            "done": "sure, uh huh, next, what?, your, ur, you're, hold, like, you, u, you are, uh uh, done",
            "next": "what?, uh huh, uh uh, your, hold, sure, next",
            "hold": "you are, u, done, uh uh, you, ur, sure, what?, you're, next, hold",
            "sure": "you are, done, like, you're, you, hold, uh huh, ur, sure",
            "like": "you're, next, u, ur, hold, done, uh uh, what?, uh huh, you, like",
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
        disp = int(disp)

        # find and output instruction and record position & label for each in an array [pos,lab]
        if i == 1:
            if disp == 1 or disp == 2:
                print("Press the button in POSITION 2")
                lab = input("What label is that? ")
                stage1 = ["2", lab]
                i += 1
            elif disp == 3:
                print("Press the button in POSITION 3")
                lab = input("What label is that? ")
                stage1 = ["3", lab]
                i += 1
            elif disp == 4:
                print("Press the button in POSITION 4")
                lab = input("What label is that? ")
                stage1 = ["4", lab]
                i += 1

        elif i == 2:
            if disp == 1:
                print("Press the button with LABEL 4")
                pos = input("What position is that? ")
                stage2 = [pos, "4"]
                i += 1
            elif disp == 3:
                print("Press the button in POSITION 1")
                lab = input("What label is that? ")
                stage2 = ["1", lab]
                i += 1
            elif disp == 2 or disp == 4:
                print(f"Press the button in POSITION {stage1[0]}")
                lab = input("What label is that? ")
                stage2 = [stage1[0], lab]
                i += 1

        elif i == 3:
            if disp == 1:
                print(f"Press the button with LABEL {stage2[1]}")
                pos = input("What position is that? ")
                stage3 = [pos, stage2[1]]
                i += 1
            elif disp == 2:
                print(f"Press the button with LABEL {stage1[1]}")
                pos = input("What position is that? ")
                stage3 = [pos, stage1[1]]
                i += 1
            elif disp == 3:
                print("Press the button in POSITION 3")
                lab = input("What label is that? ")
                stage3 = ["3", lab]
                i += 1
            elif disp == 4:
                print("Press the button with LABEL 4")
                pos = input("What position is that? ")
                stage3 = [pos, "4"]
                i += 1

        elif i == 4:
            if disp == 1:
                print(f"Press the button in POSITION {stage1[0]}")
                lab = input("What label is that? ")
                stage4 = [stage1[0], lab]
                i += 1
            elif disp == 2:
                print("Press the button in POSITION 1")
                lab = input("What label is that? ")
                stage4 = ["1", lab]
                i += 1
            elif disp == 3 or disp == 4:
                print(f"Press the button in POSITION {stage2[0]}")
                lab = input("What label is that? ")
                stage4 = ["2", lab]
                i += 1

        elif i == 5:
            if disp == 1:
                return f"Press the button with LABEL {stage1[1]}"
            elif disp == 2:
                return f"Press the button with LABEL {stage2[1]}"
            elif disp == 3:
                return f"Press the button with LABEL {stage4[1]}"
            elif disp == 4:
                return f"Press the button with LABEL {stage3[1]}"


def morse():
    morsecodedict = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
    }

    print(
        "Input the message in dots(.) and dashes(-) with each letter separated by a space: "
    )
    message = input()

    message += " "
    decipher = ""
    citext = ""
    for letter in message:
        if letter != " ":
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += " "
            else:
                decipher += list(morsecodedict.keys())[
                    list(morsecodedict.values()).index(citext)
                ]
                citext = ""

    if decipher == "shell":
        return "Press at 3.505"
    elif decipher == "halls":
        return "Press at 3.515"
    elif decipher == "slick":
        return "Press at 3.522"
    elif decipher == "trick":
        return "Press at 3.532"
    elif decipher == "boxes":
        return "Press at 3.535"
    elif decipher == "leaks":
        return "Press at 3.542"
    elif decipher == "strobe":
        return "Press at 3.545"
    elif decipher == "bistro":
        return "Press at 3.552"
    elif decipher == "flick":
        return "Press at 3.555"
    elif decipher == "bombs":
        return "Press at 3.565"
    elif decipher == "break":
        return "Press at 3.572"
    elif decipher == "brick":
        return "Press at 3.575"
    elif decipher == "steak":
        return "Press at 3.582"
    elif decipher == "sting":
        return "Press at 3.592"
    elif decipher == "vector":
        return "Press at 3.595"
    elif decipher == "beats":
        return "Press at 3.600"


def compwires():
    global lastdigit
    global batteries

    if lastdigit == "undefined":
        lastdigit = (
            "even"
            if int(input("What is the last digit of the serial number? ")) % 2 == 0
            else "odd"
        )

    if batteries == "undefined":
        batteries = int(input("How many batteries? "))

    parallel = True if int(input("Is there a parallel port? (0/1) ")) == 1 else False
    while True:
        exit = input("Enter 'e' to exit, or just press enter to continue ")
        if exit == "e":
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
                if red and blue:  # red + blue
                    if star and led:
                        print("Don't cut")
                    elif star:
                        print("Cut") if parallel else print("Don't cut")
                    elif led:
                        print("Cut") if lastdigit == "even" else print("Don't cut")

                elif red:  # just red / red + white (same)
                    if star and (not led):
                        print("Cut")
                    else:
                        print("Cut") if batteries > 2 else print("Don't cut")

                else:  # just blue / blue + white (same)
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
            wire = (
                input(
                    "Enter the color and letter separated by a space or 'e' to stop: "
                )
                .lower()
                .split()
            )
            if wire[0] == "e":
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
                    if wire[1] == "a":
                        foundletter = True
                        if (
                            reds == 3
                            or reds == 4
                            or reds == 6
                            or reds == 7
                            or reds == 8
                        ):
                            print("Cut")
                        else:
                            print("Don't cut")

                    elif wire[1] == "b":
                        foundletter = True
                        if (
                            reds == 2
                            or reds == 5
                            or reds == 7
                            or reds == 8
                            or reds == 9
                        ):
                            print("Cut")
                        else:
                            print("Don't cut")

                    elif wire[1] == "c":
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
                    if wire[1] == "a":
                        foundletter = True
                        if blues == 2 or blues == 4 or blues == 8 or blues == 9:
                            print("Cut")
                        else:
                            print("Don't cut")

                    elif wire[1] == "b":
                        foundletter = True
                        if blues == 1 or blues == 3 or blues == 5 or blues == 6:
                            print("Cut")
                        else:
                            print("Don't cut")

                    elif wire[1] == "c":
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
                    if wire[1] == "a":
                        foundletter = True
                        if (
                            blacks == blacks == 1
                            or blacks == 2
                            or blacks == 4
                            or blacks == 7
                        ):
                            print("Cut")
                        else:
                            print("Don't cut")

                    elif wire[1] == "b":
                        foundletter = True
                        if (
                            blacks == blacks == 1
                            or blacks == 3
                            or blacks == 5
                            or blacks == 6
                            or blacks == 7
                        ):
                            print("Cut")
                        else:
                            print("Don't cut")

                    elif wire[1] == "c":
                        foundletter = True
                        if (
                            blacks == 1
                            or blacks == 2
                            or blacks == 4
                            or blacks == 6
                            or blacks == 8
                            or blacks == 9
                        ):
                            print("Cut")
                        else:
                            print("Don't cut")


def password():
    first = list(input("Enter the letters for the first letter of the password: "))
    second = list(input("Enter the letters for the second letter of the password: "))
    third = list(input("Enter the letters for the third letter of the password: "))
    fourth = list(input("Enter the letters for the fourth letter of the password: "))
    fifth = list(input("Enter the letters for the fifth letter of the password: "))

    words = [
        "about",
        "after",
        "again",
        "below",
        "could",
        "every",
        "first",
        "found",
        "great",
        "house",
        "large",
        "learn",
        "never",
        "other",
        "place",
        "plant",
        "point",
        "right",
        "small",
        "sound",
        "spell",
        "still",
        "study",
        "their",
        "there",
        "these",
        "thing",
        "think",
        "three",
        "water",
        "where",
        "which",
        "world",
        "would",
        "write",
    ]

    count = 0
    while count < 5:
        for i in range(len(words)):
            count = 0
            if list(words[i])[0] in first:
                count += 1
            if list(words[i])[1] in second:
                count += 1
            if list(words[i])[2] in third:
                count += 1
            if list(words[i])[3] in fourth:
                count += 1
            if list(words[i])[4] in fifth:
                count += 1
            if count == 5:
                return words[i]


# Game loop
while True:
    module = input("Enter module or 'e' to stop: ")
    module = module.lower()
    if module == "e":
        print(
            "\nIf you defused it, well done!\n\n..if you didn't, gl for next time lol"
        )
        break
    if "seq" in module:
        print(wireseqs())
    elif "wire" in module:
        print(wires())
    elif "button" in module:
        print(button())
    elif "keypad" in module:
        print(keypad())
    elif "simon" in module:
        print(simon())
    elif "wof" in module or "first" in module:
        print(wof())
    elif module in "memory":
        print(memory())
    elif "morse" in module:
        print(morse())
    elif "comp" in module:
        print(compwires())
    elif "pass" in module:
        print(password())

    else:
        print("Module not found")
