#coding=utf8
import random

class Hangman:

    def __init__(self):
        
        self.flag = True
       
        word_list=["lenovo","asus","apple","msi","monster","samsung","acer","hp","casper"]
        self.word_list = [item for item in word_list]
        
        
    
        self.found = [] #found letters will be added to this list
        
        self.heart = 5 #number of guesses
        
        return None
    
    def random_word(self):
        wordd= random.choice(self.word_list)
        self.wordd=wordd
  
    def init_stars(self):
        liste=['*' for i in range(len(self.wordd))]
        print("\n There are {0} letters in word".format(len(self.wordd)))
        print(''.join(liste))
        self.liste=liste
        return None
    
    def heart_counter(self):
    
        if (self.heart)!=1:
            print("\n You have {0} heart ".format(self.heart))
        else:
            print("\You have {0} heart".format(self.heart))

        return self.heart
    
    def letter(self):

        lettr=str(input("Plese enter a small letter: "))
        # lettr=lettr.lower()
        self.lettr=lettr
        
        return None
    
    def start_game(self):

        if  len(self.lettr)>1 or len(self.lettr)==0:
            print("\t\n You must write one character at a time (1 heart gone)\n")
            self.heart=self.heart - 1
        elif (self.lettr).isalpha()==False:
            print("\t\n. You entered a non-alphabet character. (1 heart gone)\n")
            self.heart=self.heart - 1
        elif self.lettr not in self.wordd:
            print("This letter doesn't exist in the word (1 heart gone.)\n")
            self.heart=self.heart - 1
        else:
            print("Right!")
            #Replace the stars with characters already in the word
            for index in range(len(self.wordd)):
                if self.lettr==self.wordd[index]:
                    self.liste[index]=self.lettr
                    
        print(''.join(self.liste))
        return None
    
    def win(self):
     
        if '*' not in self.liste:
            print("\n\n You win! This word is : {0}\n Congratulations!".format(self.wordd))
            if self.wordd not in self.found:
                (self.found).append(self.wordd) #If you found it for the first time, add it to the list
            return True
   
    def loss(self):
       
        if '*' in self.liste:
            print("\n\n You lost :(")
        return None

    def exitt():
   
        try:
            status=int(input("Enter 0 to exit the game: "))
            if status==0:
               return False
          
            else:
                print("Enter again :")
                return Hangman.exitt()
        except:
            print("Enter again:")
            return Hangman.exitt()    
    def status(self):
  
        self.flag= Hangman.exitt()
        return self.flag    

deneme=Hangman()

while deneme.flag==True:
    
    deneme.random_word()
    deneme.init_stars()
    deneme.heart_counter()
    
    while (deneme.heart) > 0:
        
        deneme.letter()
        deneme.start_game()
        deneme.heart_counter()
        
        if deneme.win()==True:
            break
        
    deneme.loss()
    deneme.status()
