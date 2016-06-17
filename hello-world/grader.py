flag = "こんにちは_世界"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."