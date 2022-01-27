############### Blackjack Project #####################
import random
import art
def play_game():

  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


  user_cards = []
  computer_cards = []
  for x in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  print(f"Your cards: {user_cards}")



  def calculate_score(List):
   if 11 in List and 10 in List and len(List)==2:
    return 0
   for x in range(0,2):
      if(List[x]==11 and sum(List)>21):
        List.remove(11)
        List.append(1)
  
   return sum(List)

  is_game_over=False
  while(is_game_over==False):
    user_score=calculate_score(user_cards)
    print(f"Your current score: {user_score}")
    computer_score=calculate_score(computer_cards)
    print(f"Computer's first card: {computer_cards[0]}")
    if(calculate_score(computer_cards)==0 or calculate_score(user_cards)==0 or calculate_score(user_cards)>21):
      print("Game Over.")
      is_game_over=True;
      break;y
    else:
      ch=input("Type 'y' to draw another card, else 'n'. ")
      if(ch=='y'):
        user_cards.append(deal_card())
        print(user_cards)
      else:
        is_game_over=True;
  while(computer_score!=0 and computer_score<17):
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  def compare(user, computer):
    if(user==computer):
      return ("Draw")
    elif(user==0):
      return ("Winner, with a Blackjack!")
    elif(computer==0):
      return ("Loser, computer had a Blackjack.")
    elif(user > 21):
      return "You went over, and you lost."
    elif(computer> 21):
      return "Opponent went over, you win."
    elif (user > computer):
      return "You win!"
    else: return "You lose, better luck next time."
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(f"User's final hand: {user_cards}, final score: {user_score}")


  print(compare(user_score, computer_score))

choice="yes"
while(choice=="yes"):
  choice=input("Do you want to play a game of BlackJack? Type 'yes' or 'no'. ")
  if(choice=="yes"):
    
    print(art.logo)
    play_game()
  else:
    print("Goodbye then!")
  

    




