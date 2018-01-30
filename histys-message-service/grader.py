#!/usr/bin/python
# -*- coding: utf-8 -*-

flag = "pudd1ng_0racl3"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "ヽ(〃･ω･)ﾉ Good job!"
	return False, "Abababababababa!"
