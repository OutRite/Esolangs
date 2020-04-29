print("Loading HQ9+...")

import datetime as dt

def BoB():
	for i in range(0, 99):
		beer = 99-i
		if beer == 1:
			print("1 bottle of beer on the wall,")
			print("1 bottle of beer.")
			print("Take one down, pass it around")
			print("No more bottles of beer on the wall")
		else:
			print("{} bottles of beer on the wall,".format(beer))
			print("{} bottles of beer.".format(beer))
			print("Take one down, pass it around")
			print("{} bottles of beer on the wall".format(beer-1))
			print("")

acc = 0

tape = input("Enter program: ").upper()

for tape_index in range(0, len(tape)):
	if tape[tape_index] == "H":
		print("hello, world")
	elif tape[tape_index] == "Q":
		print(tape)
	elif tape[tape_index] == "9":
		BoB()
	elif tape[tape_index] == "+":
		acc += 1

print("Program finished.")
print("Accumulator: {}".format(acc))