flag = "no_flag_yet"

def grade(autogen, candidate):
	if candidate == flag:
		return True, "Correct!"
	return False, "Incorrect."