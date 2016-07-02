import re

N = 520

a = open("cancer.json").read().replace(" ", "")
a = a.replace(str(N), "xxx")
a = re.sub(r"\d", "", a)
a = a.replace("xxx", str(N))

s = []
for c in a[:a.find(str(N))]:
	if c == "[":
		s.append(0)
	elif c == ",":
		s[-1] += 1
	elif c == "]":
		del s[-1]
sol = "array" + "".join(["[%d]" % d for d in s])
print sol