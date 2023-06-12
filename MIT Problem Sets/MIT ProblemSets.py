#!/usr/bin/env python
# coding: utf-8

# # Problem  Set 0

# In[1]:


import numpy as np

x = float(input("Enter number x: "))
y = float(input("Enter number y: "))
p = x**y
l = np.log2(x)
print("x**y =", format(p, '.10g'))
print("log(x) =", format(l, '.10g'))


# ## Problem  Set 1

# ## Part A: House Hunting

# In[2]:


annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0 # Initializing current savings from 0
monthly_salary =  annual_salary / 12 #Calculates monthly Salary
r = 0.04 # Annual Rate of returns from investment

months_taken = 0
while portion_down_payment > current_savings: 
    current_savings += current_savings*r/12 # Adds returns from investment
    current_savings += portion_saved * monthly_salary # Adds portion of salary
    months_taken += 1
    
print("Number of months: ", months_taken)


# ## Part B: Saving, with a raise

# In[3]:


annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
monthly_salary =  annual_salary / 12
r = 0.04

months_taken = 0
while portion_down_payment > current_savings:
    current_savings += current_savings*r/12 # Adds returns from investment
    current_savings += portion_saved * monthly_salary # Adds portion of salary
    months_taken += 1
    if months_taken % 6 == 0: # Bi-annual pay raise 
        monthly_salary *= 1 + semi_annual_raise # Calculates new monthly salary
        
#         raise = monthly_salary * semi_annual_raise
#         monthly_salary = raise + semi_annual_raise
    
print("Number of months: ", months_taken)


# ## Part C: Finding the right amount to save away

# In[4]:


def Calculate_savings_after_3_years(annual_salary, portion_saved):
    
    """ It Calculates and returns the current savings 
        after 36 months """
    
    current_savings = 0
    semi_annual_raise = 0.07
    r = 0.04
    monthly_salary = annual_salary / 12
    
    for months_taken in range(1,37,1):
        current_savings += current_savings*r/12
        current_savings += portion_saved * monthly_salary
        if months_taken % 6 == 0:
            monthly_salary *= 1 + semi_annual_raise
    
    return current_savings

annual_salary = int(input("Enter the starting salary: "))

total_cost = 1000000
portion_down_payment = 0.25 * total_cost
high = 10000
low = 0
guess = (high+low)//2
portion_saved = guess / 10000
current_savings = Calculate_savings_after_3_years(annual_salary, portion_saved)

steps = 0
while abs(portion_down_payment-current_savings) > 100 and steps < 100:
    
    if current_savings > portion_down_payment:
        high = guess
    else:
        low = guess 
            
    guess = (high+low)//2 
    portion_saved = guess / 10000
    current_savings = Calculate_savings_after_3_years(annual_salary, portion_saved)
    steps += 1
        
if  steps >= 100:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: ", portion_saved)
    print("Steps in bisection search: ", steps)


# # Problem  Set 2

# In[7]:


import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for i in secret_word:
        if i not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += str(i)
    return guessed_word

def get_available_letters(letters_guessed):
    available_letters = ''
    import string 
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            available_letters += str(i)
    return available_letters
    
    
def hangman(secret_word):
    letters_guessed = []
    u = 0
    w = 3
    g = 6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", w, "warnings left")
    print("--------")
    
    while g > 0:
        print("You have", g , "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        a = str.lower(input("Please guess a letter: "))
        
        if not str.isalpha(a):
            if w == 0:
                g -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                w -= 1
                print("Oops! That is not a valid letter. You have", w, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        elif a in letters_guessed:
            if w == 0:
                g -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                w -= 1
                print("Oops! You've already guessed that letter. You have", w, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        elif a in secret_word:
            u += 1
            letters_guessed.append(a)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(a)
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            g -= 1
        print("--------")
        
        if is_word_guessed(secret_word, letters_guessed):
            break
            
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", g*u)
    else:
        print("Sorry, you ran out of guesses. The word was "+str(secret_word)+".")  
         
        
# -------------------------------------------------------------------------------------


def match_with_gaps(my_word, other_word):
    my_word_gapless = ""
    
    for i in my_word:
        my_word_gapless += i.strip()
    
    if len(my_word_gapless) == len(other_word):
        for i in range(0,len(my_word_gapless),1):
            if my_word_gapless[i] == "_" and other_word[i] not in my_word_gapless:
                pass
            elif my_word_gapless[i] != other_word[i]:
                return False
        return True
    return False


def show_possible_matches(my_word):
    word_list = load_words()
    possible_matches = ""
    for i in word_list:
        if match_with_gaps(my_word, i):
            possible_matches += (i+" ")
            
    if possible_matches == "":
        return "No matches found"
    else:
        return possible_matches



def hangman_with_hints(secret_word):
    letters_guessed = []
    u = 0
    w = 3
    g = 6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", w, "warnings left")
    print("--------")
    
    while g > 0:
        print("You have", g , "guesses left.")
        print("Available letters: ", get_available_letters(letters_guessed))
        a = str.lower(input("Please guess a letter: "))
        if a == "*":
            print("Possible word matches are:")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        
        elif not str.isalpha(a):
            if w == 0:
                g -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                w -= 1
                print("Oops! That is not a valid letter. You have", w, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        elif a in letters_guessed:
            if w == 0:
                g -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                w -= 1
                print("Oops! You've already guessed that letter. You have", w, "warnings left:", get_guessed_word(secret_word, letters_guessed))
        elif a in secret_word:
            u += 1
            letters_guessed.append(a)
            print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
        else:
            letters_guessed.append(a)
            print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
            g -= 1
        print("--------")
        
        if is_word_guessed(secret_word, letters_guessed):
            break
            
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        print("Your total score for this game is:", g*u)
    else:
        print("Sorry, you ran out of guesses. The word was "+str(secret_word)+".")  


if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

#     secret_word = choose_word(wordlist)
#     hangman_with_hints(secret_word)

