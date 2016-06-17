flag = "tfw_kirito_is_an_osu_meme"

def grade(autogen, candidate):
	if candidate == flag:
		return True, "Correct!"
	return False, "Incorrect."