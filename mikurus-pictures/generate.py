import random
import string

password = "why_kyon_whyyy"
words = open("words.txt").read().split("\n")

random.seed(123456)

passwords = [ password ] * 4
for i in range(120):
	passwords.extend(["_".join(random.sample(words, 3))] * random.choice([ 3, 5, 7, 9 ]))

random.shuffle(passwords)

out = open("keylog.txt", "w")
for password in passwords:
	for c in password:
		wrong_chars = random.choice([0] * 20 + [1] * 10 + [2] * 5 + [3] * 3 + [4] * 2)
		out.write("".join([random.choice(string.lowercase) for i in range(wrong_chars)]))
		out.write("\x08" * wrong_chars)
		out.write(c)
	out.write("\n")
out.close()