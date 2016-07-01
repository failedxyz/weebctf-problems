flag = "only_eight_monsters_remained_i_recommend_everything_that_i_have_made_a_problem_for"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."
