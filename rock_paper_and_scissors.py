import random
outcome = ["r","s","p"]
computer_point=0
user_point=0

while True:
	user = input("Enter your output: ")
	computer = random.choice(outcome)
	print(f"You chose " + user +" While the computer chose " + computer)
	
	if user=="r" and computer=="p":
		computer_point+=1
		print("The computer won")
	elif user=="p" and computer=="r":
		user_point+=1
		print("The user won this game")
	elif user=="s" and computer=="p":
		user_point+=1
		print("The user won this game")
		
	elif user=="p" and computer=="s":
		computer_point+=1
		print("The computer won this game")
	elif user=="s" and computer=="r":
		computer_point+=1
		print("The computer won")
	elif user=="r" and computer=="s":
		user_point+=1
		print("The user won")
	else:
	    computer_point+=0
	    user_point+=0
	    print("Its a tie")
	
	print("The user has %d point and the computer has %d point "%(user_point,computer_point))
	play_again= input("Enter (y/n): ")
	if play_again!="y":
		break
	else:
		continue
	