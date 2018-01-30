flag = "1o0_pUshup5_10O_siTUps_100_sQuats_4nd_10_km_of_ruNNin9"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Correct!"
	return False, "Incorrect."
