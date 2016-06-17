flag = "tfw_kirito_is_an_osu_meme"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."