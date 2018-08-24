import collections

tags = {}
words = {}
transitions={}
emissions={}




def preproces(file):
	with open(file, "r") as line:
		sentences = line.readlines()
		for sentence in sentences:
			temp_words = sentence.split()
			prev_tag = "start"
			for word in temp_words:
				actual = word.split("/")
				temp_tags = prev_tag + "/" + actual[1]
				prev_tag = actual[1]

				if temp_tags in transitions:
					transitions[temp_tags] = transitions[temp_tags] + 1
				else:
					transitions[temp_tags] = 1

				if actual[0] in words:
					words[actual[0]] = words[actual[0]] + 1
				else:
					words[actual[0]] = 1

				if actual[1] in tags:
					tags[actual[1]] = tags[actual[1]] + 1
				else:
					tags[actual[1]] = 1

				if word in emissions:
					emissions[word] = emissions[word] + 1
				else:
					emissions[word] = 1


def transition():
	with open(file, "r") as line:
		sentences = line.readlines()



def emission():
	for w in words:
		for t in tags:
			word_tag = w + "/" + t
			if word_tag not in emissions:
				emissions[word_tag] = 0
			else:
				emissions[word_tag] = emissions[word_tag] / tags[t]

file = "example/train.txt"
preproces(file)
emission()
for k in transitions:
	print(k,transitions[k])
