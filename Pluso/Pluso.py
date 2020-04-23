print("Loading Pluso...")

import sys
import datetime as dt
charset = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
acc = 1
out = ""

def execute(cmd, acc):
	if cmd == "p":
		acc += 1
		acc = acc % 27
		out = ""
	elif cmd == "o":
		out = charset[acc]
	return [acc, out]

print("Enter script:")
tape = input().lower()

began = dt.datetime.now().microsecond

for tape_index in range(0, len(tape)):
	pluso_out = execute(tape[tape_index], acc)
	acc = pluso_out[0]
	# print(acc)
	out += pluso_out[1]

time_ended = dt.datetime.now().microsecond

taken = time_ended - began

if taken > 1000:
	print("Finished in {} seconds".format(str(taken)))
else:
	print("Finished in {} ms".format(str(taken)))

print("Output:")

print(out)