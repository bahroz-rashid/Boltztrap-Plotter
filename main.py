#!/usr/bin/env python
import sys
from fermi import Fermi_Chemical
import os


class main_route():
	@staticmethod
	def extract(path_dir,t):
		temp=t+'.0000'
		result = open(os.path.join(path_dir,t+'K.txt'),'w+')
		word=[]
		with open(os.path.join(path_dir,'boltztrap.trace'),'r') as file:
			data=file.readlines()
			for line in data:
				l=line.split()
				word.append(l)
		file.close()
		for i in range(len(word)):
			if word[i][1]==temp:
				for char in word[i]:
					result.write(str(char)+'	')
				result.write('\n')	
		result.close()
		Fermi_Chemical.Fermi_energy(path_dir,t)