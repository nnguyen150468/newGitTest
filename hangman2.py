x=100

#declare variables
word='dog'
letter_left=list(word)
score_board=['_']*len(word)
stages=['','________ ','|  | ','|  O ','|  | ','| /|\ ','| / \ ','| ']
wrong_guesses=0
win=False

#welcome
print('Welcome to Hang Man!')
print('It\'s a ',len(word),'-letter word:')
print(''.join(score_board))

#loop
while wrong_guesses<len(stages)-1:
    guess=input('\nGuess a letter: ')
    if guess in letter_left:
        character_index=letter_left.index(guess)
        score_board[character_index]=guess
        letter_left[character_index]='*'
        print(''.join(score_board))
    else:
        wrong_guesses+=1
        if wrong_guesses+1==len(stages):
            print('\n'.join(stages[0:wrong_guesses+1]))
            print('You lost! The word is',word)
            break
        print('\nIncorrect!')
        print(''.join(score_board))
        print('\n'.join(stages[0:wrong_guesses+1]))
    if '_' not in score_board:
        print(''.join(score_board))
        print('Congrats! The word is',word)
        win=True
        break
