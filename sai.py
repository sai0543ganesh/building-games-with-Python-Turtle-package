
def start(letter):
    incorrect_guess=0
    letter=letter.lower()
    list=[]
    non_guessed_list = []
    original_list = []
    for i in range(len(letter)):
        list.append('_')
        non_guessed_list.append(letter[i])
        original_list.append(letter[i])
    print(list)
    hangman=["""     
      _________
     |/      |
     |      (_)
     |   
     |       
     |      
     |
     |___
 """,
       """
        _________
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
     |___
 """    ,
             """
        _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___
 """,
             """
        _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___
 """
             ,"""
        _________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
     |___
 """]
    while(True):
        print("Guess the letter")
        guessed=input("").lower()
        if guessed in non_guessed_list:
            print("Hurray now guess the next letter")
            non_guessed_list.remove(guessed)
            count=0
            for i in original_list:
                if(i==guessed):
                    break
                count+=1
            list[count]=guessed
            print(list)
        else:
            incorrect_guess+=1
            print(f"oo sorry its incorrect remaining chances are {5-incorrect_guess}")
            print(hangman[incorrect_guess-1])
        if(incorrect_guess==6):
            print("Better luck next time")
            break
input_string=input("")
start(input_string)
