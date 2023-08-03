#Auther: (Jefferson Kurtz
#Date(8/2/23)
#Tarot card reading program
import random
import time
#print intro
print("Welcome curious soul")
time.sleep(2)
#define cards 1 good 2 bad
def get_card():
    cards = {
        1: "\n\nInquiring Mind \n\nAccording to the tarot, you're in the midst of a period of perplexity and doubt \n\nYour current uncertainty is only temporary, however \n\nThe cards predict that you'll soon find your footing \n\nHave faith in the path you're on \n\nEverything is working out for you \n\nAlways try to see things in a positive light and be open to new possibilities \n\nThe road ahead is paved with happiness and success \n\nHave faith in yourself... \nand the universe \n\nGood things are coming your way!",
        2: "\n\nInquiring Mind\n\nAccording to the tarot you are in grave danger!\n\nYour current uncertainty will only lead you down the wrong path\n\nHowever,the cards predict that you will soon be left to make an important decision\n\nDo not trust the advice of those around you\n\nFor they do not understand the consequences you are facing\n\nWhile it may seam everything is working against you\n\nYou must try to see things from another perspective and be open to new guidance\n\nWith change you can get yourself out of this mess\n\nThe road ahead is paved with sorrow and many challenges\n\n\nYou have caused this negitivity...\n\nand now the universe is punishing you\n\n\n Beware of things to come!"
    }
  #return random card
    return cards[random.randint(1, 2)]
#ask user if they want cards read
def main():
    answer = input("\nWould you like to have your cards read today? (yes/no): ").lower()
   #if elif else defined 
    if answer == "yes":
        card = get_card()
        print("\nGood...now let me see what the cards hold for you")
        time.sleep(2)
        print("\n\nThe cards say......")
        time.sleep(2)
        print (card)
    elif answer == "no":
        print("\n\nOh afraid of the cards are we?")
        time.sleep(2)
        print("\nWell then, Goodbye!")
    else:
        print("\n\nYou have confused even me!")
        time.sleep(1)
        print("\nTry again!")
 
if __name__ == "__main__":
    main()
