#!/usr/bin/python
# -*- coding: utf-8 -*-

flag = "hyperd1mensi0n_neptun1a_is_t3h_gr8est"

def grade(autogen, candidate):
	if candidate.find(flag) >= 0:
		return True, "Way to go!"
	return False, "Nope."
