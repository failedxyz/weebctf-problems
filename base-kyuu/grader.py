flag = 's4NsHa1n_hyP3!!'

def grade(autogen, candidate):
        if candidate.find(flag) >= 0:
                return True, "Correct!"
        return False, "Incorrect."
