hangman_word = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
hanged = '''
      _______
     |/      |      
     |       O
     |      \|/   
     |       |  
     |      / \  
     |
    _|___
              ''' 
one_life_left = '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |      / 
    _|___
'''
two_lives_left = '''
      _______
     |/      |
     |       O
     |      \|/
     |       |
     |       
    _|___
'''
three_lives_left = '''
      _______
     |/      |
     |       O
     |      \|/
     |       
     |       
    _|___
'''
four_lives_left = '''
      _______
     |/      |
     |       O
     |       |
     |       
     |       
    _|___
'''
five_lives_left = '''
      _______
     |/      |
     |       O
     |       
     |       
     |       
    _|___
'''
alive = '''
      _______
     |/      |
     |      
     |      
     |       
     |       
    _|___
'''
win = '''
\ O /  
  |   
 / \  
'''
game_pic = [hanged,one_life_left,two_lives_left,three_lives_left,four_lives_left,five_lives_left,alive,win]