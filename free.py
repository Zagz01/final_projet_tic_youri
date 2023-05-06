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

    randomList = ["abricot", "boussole", "crocodile", "dentelle", "émeraude", "frisson", "guitare", "horloge", "iridescence", "jonglage"]

    selectRandom = []
    
    letre = []
    
    wrongLetre = []

    wordRandom = random.choice(randomList)
    
    occurence = ""
    
    tries = 0
    
    fintPartie = 7
    
    lenght = len(wordRandom)

    for x in wordRandom:
        appendRandom = selectRandom.append(x)
    
    for i in selectRandom:
        occurence = occurence + "_ "
    
    print("This is the hang man game!")
    
    while fintPartie > 0:
            # lenght = occurence.count("_")
#             print(f"there is still {lenght} to discover")

            
            while True:
                lenght = occurence.count("_")
                print(f"there is still {lenght} to discover")
                print(wordRandom)
                
                guessWord = str(input(f'''
Please guess the word!
{occurence}
''').lower())
                if len(guessWord) > 1:
                    print('''
please enter only one letter, this will not count as a try but will count as play''')
                elif not guessWord.isalpha():
                    print('''
only letters are accepted, this will not count as a try but will count as play''')
                else:
                    break
                
            for x in guessWord:
                if x in selectRandom and x not in letre:
                    appendLetter = letre.append(x)
                    print('''
Congratulation that was the correct letter''')
                    if x not in selectRandom:
                        print(f'''
Wrong letter, you still have {fintPartie} time(s) to play''')
                        fintPartie -= 1
                elif x in letre:
                    print("You already tried this letter, this will not count as a try but will count as play")
                if x not in selectRandom and x not in wrongLetre: 
                    appendWrongLetre = wrongLetre.append(x)
                    fintPartie -= 1
                    print(f'''
Wrong letter, you still have {fintPartie} time(s) to play''')
                elif x in wrongLetre:
                    print("You already tried this letter, this will not count as a try but will count as play")                      
                                
                if fintPartie == 6:
                        print(drawings[0])
                if fintPartie == 5:
                        print(drawings[1])
                if fintPartie == 4:
                        print(drawings[2])
                if fintPartie == 3:
                        print(drawings[3])
                if fintPartie == 2:
                        print(drawings[4])
                if fintPartie == 1:
                        print(drawings[5])
                if fintPartie == 0:
                        print(drawings[6])
                        print("You lost the game")
                        break
                    
                tries += 1
                print(f'''
You played {tries} time(s)''')
            newOccurence = []
            for i in selectRandom:
                if i in letre:
                    newOccurence.append(i)
                else:
                    newOccurence.append("_")
            occurence = " ".join(newOccurence)
            
            
            if "_" not in occurence:
                print(f"You won the game the word was {wordRandom}")
                break
hangMan()