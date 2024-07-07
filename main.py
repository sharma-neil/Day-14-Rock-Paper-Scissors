from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E")

player1 = input("Player 1, select your move (R, P or S): ")
while player1 != "R" and player1 != "P" and player1 != "S":
  player1 = input("Player 1, select your move (R, P or S): ")

player2 = input("Player 2, select your move (R, P or S): ")
while player2 != "R" and player2 != "P" and player2 != "S":
  player2 = input("Player 2, select your move (R, P or S): ")

if player1 == "R":
  if player2 == "S":
    print("Player 1 wins!")
  elif player2 == "P":
    print("Player 2 wins!")
  else:
    print("It's a tie")
elif player1 == "S":
  if player2 == "P":
    print("Player 1 wins!")
  elif player2 == "R":
    print("Player 2 wins!")
  else:
    print("It's a tie")
elif player1 == "P":
  if player2 == "R":
    print("Player 1 wins!")
  elif player2 == "S":
    print("Player 2 wins!")
  else:
    print("It's a tie")
else:
  print("Something went wrong")