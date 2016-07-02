import random

MAX = 20000

with open("cancer.json", "w") as f:
	level = 0
	stk = [0]
	a = list(range(MAX))
	random.shuffle(a)
	locate = random.randint(1, MAX)
	f.write("// Locate the number %d in the mess below:\n" % locate)
	f.write("[")
	# print locate
	for i in range(MAX):
		if random.randint(0, 5) < 3:
			level += 1
			stk.append(0)
			f.write("[")
		f.write(str(a[i]))
		# if a[i] == locate:
		# 	print "".join(["[%d]" % c for c in stk[:-1]])
		stk[-1] += 1
		if (level > 0 and random.randint(0, 5) < 5 and stk[-1] >= MAX // 50) or (len(stk) > 2 and sum(stk) > MAX // 10):
			level -= 1
			del stk[-1]
			f.write("]")
		if i != MAX - 1:
			f.write(", ")
	if level > 0:
		f.write("]" * level)
	f.write("]")
	f.close()