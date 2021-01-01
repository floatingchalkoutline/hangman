class Hangman:
    STAGES = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

    LOGO = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    '''

    LIVES = 6


    def display_spaces(self, answer):
        '''Returns a series of blank spaces representing letters in the random word'''
        display = []
        for letter in answer:
            display += "_"
        return display


    def modify_answer_display(self, display, guess, answer):
        '''Takes the current display, with blank spaces, and fills in correctly guessed letters.'''
        i = 0
        for letter in answer:
            if guess == letter:
                display[i] = guess
            i += 1
        return display


    def check_loss(self, lives):
        '''Returns False when the player loses.'''
        if lives < 0:
            print("You lose!")
            return False
        else:
            return True


    def check_win(self, display):
        '''Returns False when the player wins.'''
        if "_" not in display:
            print("".join(display))
            print("You win!")
            return False
        else:
            return True