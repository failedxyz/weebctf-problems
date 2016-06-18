flag = "venalcantos_420_in_ozzeau_averdidect"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."
