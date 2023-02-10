import random

x = "1"

while x == "1":

	no = random.randint(1, 6)

	if no == 1:
		print("[-----]")
		print("[	  ]")
		print("[  0  ]")
		print("[	  ]")
		print("[-----]")
	if no == 2:
		print("[-----]")
		print("[  0  ]")
		print("[	  ]")
		print("[  0  ]")
		print("[-----]")
	if no == 3:
		print("[-----]")
		print("[	  ]")
		print("[0 0 0]")
		print("[	  ]")
		print("[-----]")
	if no == 4:
		print("[-----]")
		print("[ 0 0 ]")
		print("[	  ]")
		print("[ 0 0 ]")
		print("[-----]")
	if no == 5:
		print("[-----]")
		print("[ 0 0 ]")
		print("[  0  ]")
		print("[ 0 0]")
		print("[-----]")
	if no == 6:
		print("[-----]")
		print("[0 0 0]")
		print("[	  ]")
		print("[0 0 0]")
		print("[-----]")

	x = input("press 1 to roll again and 0 to exit:")
	print("\n")

