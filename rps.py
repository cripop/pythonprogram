import random
l=["r","p","s"]
while True:		
	#TAKE INPUT FROM USER
	u=input("enter your choice,print n to discontinue")
	#to exit
	if u=="n":
		print("game over")
		exit()
	#input from computer
	c=random.choice(l)	
	print("computer chooses",c)

	#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r"	and c=="p":
		print("computer wins")
	elif u=="p" and c=="r":
		print("user wins")
	elif u=="s"	and c=="r":
		print("computer wins")
	elif u=="r"	and c=="s":
		print("user wins")
	elif u=="p" and c=="s":
		print("computer wins")
	elif u=="s" and c=="p":
		print("user wins")
