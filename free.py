def hangMan():
    import random
    drawings =['''
|| 
||
||
|| 
||
||
||\\
||=================
''','''
||===========Y===== 
||/
||
|| 
||
||
||\\
||=================
''','''
||===========Y===== 
||/          |
||
|| 
||
||
||\\
||=================
''','''
||===========Y=== 
||/          |
||           |
|| 
||
||
||\\
||=================
''','''
||===========Y=== 
||/          |
||           |
||           0
||          /|\\
||
||\\
||=================
''','''
||===========Y=== 
||/          |
||           |
||           0
||          /|\\
||          /
||\\    
||=================
''','''
||===========Y=== 
||/          |
||           |
||           0
||          /|\\
||          / \\
||\\      
||=================
'''
    ]

    randomList = ["apricot", "compass", "crocodile", "lace", "emerald", "shiver", "guitar", "clock", "iridescence", "juggling"]

    selectRandomWord = []
    
    letter = []
    
    wrongletter = []

    wordRandom = random.choice(randomList)
    
    hiddenWord = ""
    
    tries = 0
    
    failTries = 7
    
    lenght = len(wordRandom)

    for x in wordRandom:
        appendRandom = selectRandomWord.append(x)
    
    for i in selectRandomWord:
        hiddenWord = hiddenWord + "_ "
    
    print("This is the hang man game!")
    
    while failTries > 0:
            # lenght = hiddenWord.count("_")
#             print(f"there is still {lenght} to discover")

            
            while True:
                lenght = hiddenWord.count("_")
                print(f"There is still {lenght} to discover")
                print(wordRandom)
                
                guessWord = str(input(f'''
Please guess the word!
{hiddenWord}
''').lower())
                if len(guessWord) > 1:
                    print('''
Please enter only one letter, this will not count''')
                elif not guessWord.isalpha():
                    print('''
Only letters are accepted, this will not count''')
                else:
                    break
                
            for x in guessWord:
                if x in selectRandomWord and x not in letter:
                    appendLetter = letter.append(x)
                    print('''
Congratulation that was the correct letter''')
                    if x not in selectRandomWord:
                        print(f'''
Wrong letter, you still have {failTries} trie(s) to play''')
                        failTries -= 1
                elif x in letter:
                    print("You already tried this letter, this will not count as a try but will count as play")
                if x not in selectRandomWord and x not in wrongletter: 
                    appendWrongletter = wrongletter.append(x)
                    failTries -= 1
                    print(f'''
Wrong letter, you still have {failTries} trie(s) to play''')
                elif x in wrongletter:
                    print("You already tried this letter, this will not count as a try but will count as play")                      
                                
                if failTries == 6:
                        print(drawings[0])
                if failTries == 5:
                        print(drawings[1])
                if failTries == 4:
                        print(drawings[2])
                if failTries == 3:
                        print(drawings[3])
                if failTries == 2:
                        print(drawings[4])
                if failTries == 1:
                        print(drawings[5])
                if failTries == 0:
                        print(drawings[6])
                        print("You lost the game")
                        break
                    
                tries += 1
                print(f'''
You played {tries} time(s)''')
            newhiddenWord = []
            for i in selectRandomWord:
                if i in letter:
                    newhiddenWord.append(i)
                else:
                    newhiddenWord.append("_")
            hiddenWord = " ".join(newhiddenWord)
            
            
            if "_" not in hiddenWord:
                print(f"You won the game the word was {wordRandom}")
                break
            
            
hangMan()