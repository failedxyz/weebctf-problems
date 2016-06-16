flag = "why_kyon_whyyy"

def grade(autogen, candidate):
	if candidate == flag:
		return True, "Correct!"
	return False, "Incorrect."