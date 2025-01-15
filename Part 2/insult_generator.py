from random import choice

adjectives = ['Stupid', 'Ugly', 'Clumsy', 'Useless', 'Foolish', 'Disappointing', 'Shy', 'Arrogant', 'Annoying', 'Backward', 'Greedy', 'Boring', 'Mean-spirited', 'Cruel', 'Conceited', 'Whiny', 'Rude', 'Insensitive', 'Impudent', 'Weak']

noun = ['Idiot', 'Fool', 'Moron', 'Imbecile', 'Buffoon', 'Jerk', 'Loser', 'Coward', 'Hypocrite', 'Scoundrel', 'Failure', 'Simpleton', 'Clown', 'Brute', 'Creep', 'Bully', 'Rat', 'Weasel', 'Dope', 'Lowlife']

name = input ("What is your name? = ")

def print_insult() :
     print ("You're a "+ choice(adjectives) + " "+choice(noun))

answer = ""
while (answer != "no") :
     if name == 'Andro':
          print("You're Awesome Man!")
     else :
          print_insult()
     answer = input("Can you take anymore? : ")