
def wordle():
    import random 
    from colorama import Fore, Back, Style

    lines = ['']
    with open('words.txt', 'r') as file:
        words_list = file.readlines()
    words_list= [eachWord.strip() for eachWord in words_list]
    word = random.choice(words_list).casefold()
    
    
    guess = False
    guessNumber = 1
    print('Guess the five-letter word in five tries. GREEN letter =  RIGHT letter & RIGHT position - RED letter = RIGHT letter but WRONG position.')
    l = []
    
    while guess == False:
        userGuesses = str(input('Guess {}: '.format(guessNumber)))
        userGuess = userGuesses.casefold()
        guessNumber += 1
        
    
            
        for letter in userGuess:
            l.clear()
            l.append(letter)
            
            if len(userGuess) != 5:
                print ('The word must be 5 letters! Try Again!')
                guessNumber -= 1
                break
            if letter == userGuess[0] and letter == str(word[0]) and l.count(letter)<2:
                print(Fore.GREEN + letter, end = ' ')
                continue
            if letter == userGuess[1] and letter == str(word[1]) and l.count(letter)<2:
                print(Fore.GREEN + letter, end = ' ')
                continue
            if letter == userGuess[2] and letter == str(word[2]) and l.count(letter)<2:
                print(Fore.GREEN + letter, end = ' ')
                continue
            if letter == userGuess[3] and letter == str(word[3]) and l.count(letter)<2:
                print(Fore.GREEN + letter, end = ' ')
                continue
            if letter == userGuess[4] and letter == str(word[4]) and l.count(letter)<2:
                print(Fore.GREEN + letter, end = ' ')
                continue
            if letter in str(word) and l.count(letter)<4:
                print(Fore.RED + letter, end = ' ')
                continue
      
                
          
            
            
        if guessNumber == 6 and userGuess == userGuess == str(word):
            print('{} is correct! Good job!'.format(word))
            break
        if guessNumber == 6 and userGuess != str(word):
            print ('Game over! the correct answer was {}.'.format(word))
            break
        if userGuess == str(word):
            print('{} is correct! Good job!'.format(word))
            break
  


wordle ()
