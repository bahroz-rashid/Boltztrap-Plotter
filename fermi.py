import os
import sys


def Bohr_to_Ang(ang):
	bohr= ang * ((0.529177249)**3)*(10**(-24)) 
	return bohr

class Fermi_Chemical():
	@staticmethod
	def Fermi_energy(path_dir,t):
		with open(os.path.join(path_dir,'boltztrap.intrans'),'r') as file:
			data=file.readlines()
			e=data[2].split()
			Ef=float(e[0])
		file.close()
		word=[]
		with open(os.path.join(path_dir,t+'K.txt'),'r+') as file:
			data=file.readlines()
			for line in data:
				l=line.split()
				word.append(l)
		file.close()
		with open(os.path.join(path_dir,'boltztrap.outputtrans'),'r') as file:
			data_2=file.readlines()
		file.close()
		for line2 in data_2:
			e=line2.split()
			if e!=[]:
				if e[0]=='VOLUME:':
					volume_a=e[1]
		volume_b=Bohr_to_Ang(float(volume_a))
		w=word
		u=[]
		with open(os.path.join(path_dir,t+'K.txt'),'r+') as file:	
			for i in range(len(w)):
				u=str(13.6*(float(w[i][0])-Ef))
				v=str(float(w[i][2])/(volume_b))
				w[i].append(u)
				w[i].append(v)
				for char in w[i]:
					file.write(str(char)+'	')
				file.write('\n')
		file.close()	