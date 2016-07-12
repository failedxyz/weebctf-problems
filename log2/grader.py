flag = "hooray_l0g_lo9_lOg_LOG_FROM_BLAMMO"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."
