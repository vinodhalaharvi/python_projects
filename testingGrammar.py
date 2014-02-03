# Expanding Exp
# This is very, very difficult.

grammar = [
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

def expand(tokens, grammar):
	for pos in range(len(tokens)): # for every token
		for rule in grammar: # compare for every rule in the grammar
			if tokens[pos]==rule[0]:
				yield tokens[0:pos] + rule[1] + tokens[pos+1:]

depth = 2 

line = "this is a test exp inside some string"
utterances = [line.split(),]

for x in range(depth):
	for sentence in utterances:
		utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
	print sentence
